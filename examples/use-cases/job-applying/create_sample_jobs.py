import pandas as pd

def create_sample_jobs_csv():
    """Create a sample jobs CSV file with Greenhouse jobs."""
    jobs = [
        {
            'Job Title': 'Customer Success/Support',
            'Company': 'Greenhouse',
            'URL': 'https://www.greenhouse.com/careers/opportunities/job?id=2154269',
            'Location': 'United States',
            'Salary Range': 'Competitive'
        },
        {
            'Job Title': 'Senior Customer Success Manager, Enterprise',
            'Company': 'Greenhouse',
            'URL': 'https://www.greenhouse.com/careers/opportunities/job?id=6531244',
            'Location': 'British Columbia',
            'Salary Range': '$83,800 - $111,732'
        },
        {
            'Job Title': 'Customer Success Manager',
            'Company': 'Greenhouse',
            'URL': 'https://www.greenhouse.com/careers/opportunities/job?id=2155033',
            'Location': 'Remote',
            'Salary Range': 'Competitive'
        }
    ]
    
    df = pd.DataFrame(jobs)
    df.to_csv('sample_jobs.csv', index=False)
    print("Created sample_jobs.csv with Greenhouse jobs")

if __name__ == "__main__":
    create_sample_jobs_csv() 