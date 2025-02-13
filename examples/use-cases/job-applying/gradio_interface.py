import gradio as gr
import asyncio
from pathlib import Path
from job_application_agent import JobApplicationAgent
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class JobApplicationUI:
    def __init__(self):
        try:
            self.agent = JobApplicationAgent(
                database_path=Path("jobs_database.xlsx"),
                config_path=Path("config/personal_info.yaml"),
                resume_path=Path("data/resume.pdf")
            )
            logger.info("Agent initialized successfully!")
            self.current_url = None  # Add this to store current URL
        except Exception as e:
            logger.error(f"Error initializing agent: {str(e)}")
            self.agent = None
            
    def check_agent(self):
        """Check if agent is properly initialized."""
        if not self.agent:
            raise ValueError("Agent not initialized properly. Please check the logs for errors.")

    def add_job(self, url: str) -> str:
        """Add a single job URL to the database."""
        try:
            self.check_agent()
            job_id = self.agent.manager.add_job(
                title="Greenhouse Position",
                company="Greenhouse",
                url=url
            )
            return f"Added job with URL: {url}"
        except Exception as e:
            return f"Error adding job: {str(e)}"
    
    async def prepare_and_review(self, url: str):
        """Prepare application for review."""
        try:
            self.check_agent()
            self.current_url = url  # Store URL for submission
            result = await self.agent.prepare_application(url)
            return f"""
            Analyzing job at: {url}
            
            Form Analysis:
            {result.get('form_analysis', 'No form analysis available')}
            
            Prepared Application:
            {result['prepared_data']}
            
            {'Error: ' + result['error'] if result['error'] else ''}
            """
        except Exception as e:
            self.current_url = None
            return f"Error preparing application: {str(e)}"
    
    async def submit_application(self, url: str, approved: bool) -> str:
        """Submit the approved application."""
        try:
            self.check_agent()
            if not approved:
                return "Please check 'Approve Submission' before submitting"
            
            if url != self.current_url:
                return "URL mismatch. Please analyze the job again."
            
            result = await self.agent.submit_application(url, approved)
            self.current_url = None  # Clear URL after submission
            return f"Success: {result.extracted_content}" if not result.error else f"Error: {result.error}"
        except Exception as e:
            self.current_url = None
            return f"Error submitting application: {str(e)}"

def create_ui():
    ui = JobApplicationUI()
    
    with gr.Blocks() as app:
        gr.Markdown("""
        # 🤖 Automated Job Application Assistant
        
        1. Enter the Greenhouse job URL
        2. Review the prepared application
        3. Submit if everything looks good
        """)
        
        with gr.Row():
            job_url = gr.Textbox(
                label="Greenhouse Job URL",
                placeholder="https://www.greenhouse.com/careers/opportunities/job?id=..."
            )
            add_btn = gr.Button("Add & Analyze Job")
        
        status_output = gr.Textbox(label="Status", lines=1)
        
        gr.Markdown("### Application Preview")
        preview_output = gr.Textbox(label="Application Details", lines=15)
        
        with gr.Row():
            approve_checkbox = gr.Checkbox(label="Approve Submission")
            submit_btn = gr.Button("Submit Application", variant="primary")
        
        submit_output = gr.Textbox(label="Submission Result", lines=3)
        
        # Event handlers
        add_btn.click(
            ui.add_job,
            inputs=[job_url],
            outputs=[status_output]
        ).success(
            lambda url: asyncio.run(ui.prepare_and_review(url)),
            inputs=[job_url],
            outputs=[preview_output]
        )
        
        submit_btn.click(
            lambda url, approved: asyncio.run(ui.submit_application(url, approved)),
            inputs=[job_url, approve_checkbox],
            outputs=[submit_output]
        )
    
    return app

if __name__ == "__main__":
    app = create_ui()
    app.launch() 