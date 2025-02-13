from pathlib import Path
from setup_job_application import setup_application_environment
from job_application_manager import JobApplicationManager

def test_job_application_system():
    # Setup the environment
    base_dir = Path(__file__).parent
    db_path, config_path = setup_application_environment(base_dir)
    
    # Initialize manager
    manager = JobApplicationManager(db_path, config_path)
    
    # Add a test job
    job_id = manager.add_job(
        title="Senior Python Developer",
        company="Tech Corp",
        url="https://example.com/jobs/123",
        location="Remote",
        salary="$120k-150k",
        description="Looking for a senior Python developer..."
    )
    
    # Update status
    manager.update_job_status(
        job_id=job_id,
        status="Applied",
        notes="Applied via company website"
    )
    
    # Get stats
    stats = manager.get_application_stats()
    print("\nApplication Stats:")
    for key, value in stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    test_job_application_system() 