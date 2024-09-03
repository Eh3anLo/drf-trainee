from datetime import datetime
import subprocess
import os
from celery import Celery

# Define your periodic task
app = Celery()


@app.task
def backup_database():
    # Define your database credentials
    db_user = os.getenv('POSTGRES_USER')
    db_name = os.getenv('POSTGRES_DB')
    db_host = os.getenv('POSTGRES_HOST')
    db_port = os.getenv('POSTGRES_PORT', '5432')
    db_password = os.getenv('POSTGRES_PASSWORD')

    # Create the backup file name
    backup_file = f"./backups/db_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    # Run the pg_dump command
    try:
        print('\a')
        subprocess.run(
            [
                "pg_dump",
                "-c",
                "-C",
                f"--dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
                "-f", backup_file
            ],
            check=True
        )
        print(f"Backup successful: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")
