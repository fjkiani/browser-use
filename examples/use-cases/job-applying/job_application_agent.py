import asyncio
import os
from pathlib import Path
from typing import Optional, List
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller, ActionResult
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext
from job_application_manager import JobApplicationManager
import logging
import subprocess
import platform

# Load environment variables
load_dotenv()

# Setup logging
logger = logging.getLogger(__name__)

# Kill any existing Chrome processes before initializing
try:
    system = platform.system()
    if system == "Darwin":  # macOS
        subprocess.run(['pkill', '-9', 'Google Chrome'])
        subprocess.run(['pkill', '-9', 'chrome'])
    elif system == "Linux":
        subprocess.run(['pkill', '-9', 'chrome'])
    elif system == "Windows":
        subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'], shell=True)
except:
    pass  # Ignore errors from pkill

# Initialize shared controller
controller = Controller()

class JobApplicationAgent:
    def __init__(self, 
                 database_path: Path,
                 config_path: Path,
                 resume_path: Path):
        """Initialize the job application agent."""
        # Initialize job application manager
        self.manager = JobApplicationManager(database_path, config_path)
        
        # Set resume path
        self.resume_path = Path(resume_path)
        if not self.resume_path.exists():
            raise FileNotFoundError(f"Resume not found at {self.resume_path}")
        
        # Use shared controller only
        self.controller = controller
        
        # Register custom actions
        self._register_actions()
        
        self.current_agent = None  # Add this to store current agent
        
    def _register_actions(self):
        """Register custom actions with the controller."""
        
        @self.controller.action('Read resume for context')
        async def read_resume():
            """Read resume content for context."""
            if not self.resume_path.exists():
                return ActionResult(error=f"Resume not found at {self.resume_path}")
            
            with open(self.resume_path, 'r') as f:
                content = f.read()
            return ActionResult(extracted_content=content, include_in_memory=True)
        
        @self.controller.action('Upload resume to application form')
        async def upload_resume(browser: BrowserContext, element_index: int):
            """Upload resume to the specified form element."""
            try:
                # Get DOM element
                dom_el = await browser.get_dom_element_by_index(element_index)
                if not dom_el:
                    return ActionResult(error=f"No element found at index {element_index}")
                
                # Get file upload element
                upload_el = dom_el.get_file_upload_element()
                if not upload_el:
                    return ActionResult(error="No file upload element found")
                
                # Upload file
                await upload_el.set_input_files(str(self.resume_path.absolute()))
                return ActionResult(extracted_content="Resume uploaded successfully")
            
            except Exception as e:
                return ActionResult(error=f"Failed to upload resume: {str(e)}")
        
        @self.controller.action('Save job to database')
        async def save_job(title: str, company: str, url: str, 
                          description: Optional[str] = None,
                          location: Optional[str] = None,
                          salary: Optional[str] = None):
            """Save job details to database."""
            job_id = self.manager.add_job(
                title=title,
                company=company,
                url=url,
                description=description,
                location=location,
                salary=salary
            )
            return ActionResult(extracted_content=f"Job saved with ID: {job_id}")
        
        @self.controller.action('Update application status')
        async def update_status(url: str, status: str, notes: Optional[str] = None):
            """Update application status for a job."""
            job = self.manager.get_job_by_url(url)
            if not job:
                return ActionResult(error=f"No job found with URL: {url}")
            
            self.manager.update_job_status(job['Job ID'], status, notes)
            return ActionResult(extracted_content=f"Updated status to {status}")

        @self.controller.action('Find application form')
        async def find_form(browser: BrowserContext):
            """Find the application form by incrementally scrolling."""
            try:
                # First check if we're on the right domain
                current_url = await browser.get_current_url()
                if "greenhouse.io" not in current_url:
                    # Try to find and click the "Apply" button
                    apply_button = await browser.get_element('a[href*="greenhouse.io"]:not(.banner-link)')
                    if apply_button:
                        await apply_button.click()
                        await browser.wait_for_navigation()
                
                # Wait for form container to be visible
                form_container = await browser.wait_for_element([
                    'form.application-form',
                    '#application_form',
                    'form[action*="greenhouse"]'
                ], timeout=10000)
                
                if not form_container:
                    return ActionResult(error="Could not find application form container")
                
                # Get form fields within the container
                form_fields = await form_container.query_selector_all([
                    'input[type="text"]:not(.banner-link)',
                    'input[type="email"]:not(.banner-link)',
                    'input[type="file"]:not(.banner-link)',
                    'textarea:not(.banner-link)',
                    'select:not(.banner-link)'
                ])
                
                if form_fields:
                    field_info = []
                    for i, field in enumerate(form_fields):
                        field_type = await field.get_attribute('type')
                        field_name = await field.get_attribute('name')
                        field_id = await field.get_attribute('id')
                        field_info.append(f"Field {i}: type={field_type}, name={field_name}, id={field_id}")
                    
                    return ActionResult(
                        extracted_content="\n".join(field_info),
                        include_in_memory=True,
                        form_analysis=field_info
                    )
                
                return ActionResult(error="No form fields found in container")
                
            except Exception as e:
                return ActionResult(error=f"Error finding form: {str(e)}")

        @self.controller.action('Fill form field')
        async def fill_form_field(browser: BrowserContext, index: int, text: str):
            """Fill a form field with better targeting."""
            try:
                # Find the form container first
                form_container = await browser.get_element([
                    'form.application-form',
                    '#application_form',
                    'form[action*="greenhouse"]'
                ])
                
                if not form_container:
                    return ActionResult(error="Could not find form container")
                
                # Get input fields within the form container
                input_fields = await form_container.query_selector_all([
                    'input[type="text"]:not(.banner-link)',
                    'input[type="email"]:not(.banner-link)',
                    'textarea:not(.banner-link)'
                ])
                
                if index >= len(input_fields):
                    return ActionResult(error=f"No field found at index {index}")
                
                field = input_fields[index]
                await field.fill(text)
                
                return ActionResult(
                    extracted_content=f"Filled field {index} with {text}",
                    include_in_memory=True
                )
            except Exception as e:
                return ActionResult(error=f"Failed to fill field {index}: {str(e)}")

        @self.controller.action('Navigate to URL')
        async def navigate(browser: BrowserContext, url: str):
            """Navigate to a URL and wait for load."""
            try:
                await browser.goto(url)
                await asyncio.sleep(2)  # Wait for initial load
                return ActionResult(
                    extracted_content=f"Successfully navigated to {url}",
                    include_in_memory=True
                )
            except Exception as e:
                return ActionResult(error=f"Failed to navigate: {str(e)}")

    async def apply_to_job(self, url: str) -> ActionResult:
        """Apply to a specific job."""
        # Create task for the agent
        task = (
            "You are a professional job application assistant. "
            f"1. Go to {url}\n"
            "2. Read the job description and requirements\n"
            "3. Fill out the application form using my resume and personal information\n"
            "4. Upload my resume when needed\n"
            "5. Submit the application\n"
            "6. Update the application status in our database"
        )
        
        # Initialize agent
        agent = Agent(
            task=task,
            llm=ChatOpenAI(model="gpt-4o", api_key=os.getenv('OPENAI_API_KEY')),
            controller=self.controller,
            use_vision=True  # Enable vision capabilities
        )
        
        # Run the agent
        try:
            result = await agent.run()
            return result
        except Exception as e:
            logger.error(f"Error applying to job: {str(e)}")
            return ActionResult(error=f"Failed to apply: {str(e)}")

    async def batch_apply(self, num_jobs: int = 5) -> List[ActionResult]:
        """Apply to multiple pending jobs."""
        pending_jobs = self.manager.get_pending_applications()
        jobs_to_apply = pending_jobs.head(num_jobs)
        
        results = []
        for _, job in jobs_to_apply.iterrows():
            result = await self.apply_to_job(job['URL'])
            results.append(result)
            
            # Update status based on result
            status = "Applied" if not result.error else "Failed"
            notes = result.error if result.error else "Successfully applied"
            self.manager.update_job_status(job['Job ID'], status, notes)
        
        return results

    async def ensure_files(self):
        """Ensure all required files exist."""
        required_files = {
            'Resume': self.resume_path,
            'Database': self.manager.database_path,
            'Config': self.manager.config_path
        }
        
        missing_files = []
        for name, path in required_files.items():
            if not path.exists():
                missing_files.append(f"{name} not found at {path}")
        
        if missing_files:
            raise FileNotFoundError("\n".join(missing_files))

    async def prepare_application(self, url: str) -> dict:
        """Prepare application for review before submission."""
        try:
            task = (
                "You are a professional job application assistant for Greenhouse jobs. Follow these steps:\n"
                f"1. Use 'Navigate to URL' action to go to {url}\n"
                "2. Use 'Find application form' action to locate the application form\n"
                "3. Once the form is found, analyze the form structure:\n"
                "   - Use 'analyze_form_fields' to get form field information\n"
                "   - Only interact with actual form elements (input, textarea, select)\n"
                "   - Pay attention to field types and requirements\n"
                "4. For each identified form field:\n"
                "   - Use the correct field index from the analysis\n"
                "   - Fill required fields first\n"
                "   - Skip optional fields unless you have the information\n"
                "5. For file uploads:\n"
                f"   - Resume path: {self.resume_path}\n"
                "6. DO NOT submit the application\n"
                "7. Return all the information you plan to submit for review\n"
                "8. IMPORTANT: After filling the form:\n"
                "   - Return the filled information\n"
                "   - Keep the browser session active\n"
                "   - Do not close any windows\n"
                "   - Wait for further instructions\n"
                "\nImportant: Make sure the form is found before attempting to fill fields."
            )
            
            # Create and store agent reference
            self.current_agent = Agent(
                task=task,
                llm=ChatOpenAI(
                    model="gpt-4o", 
                    api_key=os.getenv('OPENAI_API_KEY'),
                    temperature=0.1
                ),
                controller=self.controller,
                use_vision=True
            )
            
            result = await self.current_agent.run()
            
            # Handle result properly
            if isinstance(result, ActionResult):
                return {
                    'url': url,
                    'prepared_data': result.extracted_content,
                    'error': result.error if hasattr(result, 'error') else None,
                    'form_analysis': result.form_analysis if hasattr(result, 'form_analysis') else None
                }
            else:
                return {
                    'url': url,
                    'prepared_data': str(result),
                    'error': None,
                    'form_analysis': None
                }
            
        except Exception as e:
            logger.error(f"Error preparing application: {str(e)}")
            return {
                'url': url,
                'prepared_data': None,
                'error': str(e),
                'form_analysis': None
            }

    async def submit_application(self, url: str, approved: bool = False) -> ActionResult:
        """Submit the prepared application."""
        if not approved:
            return ActionResult(error="Application not approved for submission")
            
        if not self.current_agent:
            return ActionResult(error="No prepared application found. Please analyze the job first.")
            
        try:
            submit_task = (
                "Continue with the previous application:\n"
                "1. Verify all fields are still filled\n"
                "2. Click the submit button\n"
                "3. Wait for confirmation\n"
                "4. Report the submission status"
            )
            
            # Use the same agent instance
            self.current_agent.task = submit_task
            result = await self.current_agent.run()
            
            return result
        except Exception as e:
            logger.error(f"Error submitting application: {str(e)}")
            return ActionResult(error=f"Failed to submit: {str(e)}")
        finally:
            # Only clear the agent after submission
            self.current_agent = None

# Example usage
async def main():
    # Initialize agent
    agent = JobApplicationAgent(
        database_path="jobs_database.xlsx",
        config_path="config/personal_info.yaml",
        resume_path="cv_04_24.pdf"
    )
    
    # Apply to jobs
    results = await agent.batch_apply(num_jobs=3)
    
    # Print results
    for result in results:
        if result.error:
            print(f"Error: {result.error}")
        else:
            print(f"Success: {result.extracted_content}")

if __name__ == "__main__":
    asyncio.run(main())
