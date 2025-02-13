import pandas as pd
from pathlib import Path
import yaml
import shutil

def create_job_database(output_path: Path) -> Path:
    """Create initial job database Excel file with required columns."""
    
    # Define columns with their data types
    columns = {
        'Job Title': str,
        'Company': str,
        'URL': str,
        'Status': str,  # e.g., 'Not Applied', 'Applied', 'Rejected', 'Interview'
        'Applied Date': 'datetime64[ns]',
        'Job Description': str,
        'Requirements': str,
        'Salary Range': str,
        'Location': str,
        'Application Type': str,  # e.g., 'Direct', 'LinkedIn', 'Company Website'
        'Notes': str,
        'Last Modified': 'datetime64[ns]',
        'Job ID': str  # Unique identifier for each job
    }
    
    # Create empty DataFrame with specified columns
    df = pd.DataFrame(columns=columns.keys())
    
    # Set data types for columns
    for col, dtype in columns.items():
        df[col] = df[col].astype(dtype)
    
    # Save to Excel
    df.to_excel(output_path, index=False)
    print(f"Created job database at: {output_path.absolute()}")
    
    return output_path

def create_config_directory(base_path: Path) -> Path:
    """Create config directory and personal info YAML file."""
    config_dir = base_path / "config"
    config_dir.mkdir(exist_ok=True)
    
    personal_info = {
        "personal": {
            "name": "",
            "email": "",
            "phone": "",
            "location": "",
            "linkedin": "",
            "portfolio": "",
            "github": "",
        },
        "education": [{
            "degree": "",
            "major": "",
            "school": "",
            "location": "",
            "start_date": "",
            "end_date": "",
            "gpa": "",
            "relevant_coursework": [],
            "achievements": []
        }],
        "experience": [{
            "title": "",
            "company": "",
            "location": "",
            "start_date": "",
            "end_date": "",
            "description": [],
            "technologies": [],
            "achievements": []
        }],
        "skills": {
            "technical": {
                "programming_languages": [],
                "frameworks": [],
                "databases": [],
                "tools": [],
                "cloud_platforms": []
            },
            "soft_skills": [],
            "languages": [],
            "certifications": []
        },
        "application_preferences": {
            "desired_role": [],
            "preferred_locations": [],
            "minimum_salary": "",
            "remote_preference": "",
            "notice_period": "",
            "visa_sponsorship_required": False
        },
        "cover_letter_template": """
Dear {hiring_manager},

I am writing to express my interest in the {position} role at {company}...

{custom_paragraph}

Thank you for considering my application.

Best regards,
{name}
"""
    }
    
    config_path = config_dir / "personal_info.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(personal_info, f, sort_keys=False, default_flow_style=False)
    
    print(f"Created config file at: {config_path.absolute()}")
    return config_path

def setup_application_environment(base_dir: Path):
    """Set up the complete job application environment."""
    # Create necessary directories
    base_dir.mkdir(exist_ok=True)
    
    # Create database
    db_path = base_dir / "jobs_database.xlsx"
    create_job_database(db_path)
    
    # Create config
    config_path = create_config_directory(base_dir)
    
    return db_path, config_path

if __name__ == "__main__":
    # Set up in the job-applying directory
    base_dir = Path(__file__).parent
    db_path, config_path = setup_application_environment(base_dir) 