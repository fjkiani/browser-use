import yaml
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional
import uuid

class JobApplicationManager:
    def __init__(self, 
                 database_path: Path,
                 config_path: Path):
        self.database_path = Path(database_path)
        self.config_path = Path(config_path)
        self.personal_info = self.load_personal_info()
        self.jobs_db = self.load_jobs_database()
    
    def load_personal_info(self) -> Dict:
        """Load personal information from YAML file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found at {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def load_jobs_database(self) -> pd.DataFrame:
        """Load jobs database from Excel file."""
        if not self.database_path.exists():
            raise FileNotFoundError(f"Database file not found at {self.database_path}")
        
        return pd.read_excel(self.database_path)
    
    def add_job(self, 
                title: str,
                company: str,
                url: str,
                description: Optional[str] = None,
                location: Optional[str] = None,
                salary: Optional[str] = None) -> str:
        """Add a new job to the database."""
        job_id = str(uuid.uuid4())
        new_job = {
            'Job ID': job_id,
            'Job Title': title,
            'Company': company,
            'URL': url,
            'Status': 'Not Applied',
            'Job Description': description,
            'Location': location,
            'Salary Range': salary,
            'Applied Date': None,
            'Last Modified': datetime.now(),
            'Notes': ''
        }
        
        self.jobs_db = pd.concat([self.jobs_db, pd.DataFrame([new_job])], ignore_index=True)
        self.save_database()
        return job_id
    
    def update_job_status(self, job_id: str, status: str, notes: Optional[str] = None):
        """Update job application status."""
        if job_id not in self.jobs_db['Job ID'].values:
            raise ValueError(f"Job ID {job_id} not found in database")
        
        idx = self.jobs_db[self.jobs_db['Job ID'] == job_id].index[0]
        self.jobs_db.at[idx, 'Status'] = status
        self.jobs_db.at[idx, 'Last Modified'] = datetime.now()
        
        if status == 'Applied':
            self.jobs_db.at[idx, 'Applied Date'] = datetime.now()
        
        if notes:
            self.jobs_db.at[idx, 'Notes'] = notes
        
        self.save_database()
    
    def save_database(self):
        """Save the jobs database to Excel file."""
        self.jobs_db.to_excel(self.database_path, index=False)

    def get_pending_applications(self) -> pd.DataFrame:
        """Get all jobs that haven't been applied to yet."""
        return self.jobs_db[self.jobs_db['Status'] == 'Not Applied']
    
    def get_applied_jobs(self) -> pd.DataFrame:
        """Get all jobs that have been applied to."""
        return self.jobs_db[self.jobs_db['Status'] == 'Applied'] 