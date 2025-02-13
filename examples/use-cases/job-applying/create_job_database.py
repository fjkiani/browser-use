import pandas as pd
from pathlib import Path

def create_job_database(output_path: str = "jobs_database.xlsx"):
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
    output_file = Path(output_path)
    df.to_excel(output_file, index=False)
    print(f"Created job database at: {output_file.absolute()}")
    
    return output_file

if __name__ == "__main__":
    create_job_database() 