import os
import glob
import subprocess
from datetime import datetime
from decouple import config
db_user = config('POSTGRES_USER')
db_name = config('POSTGRES_DB')
db_host = config('POSTGRES_HOST')
db_port = config('POSTGRES_PORT', '5432')
db_password = config('POSTGRES_PASSWORD')

list_backup_files = glob.glob('/src/backups/*.sql')
latest_backup = max(list_backup_files, key=os.path.getctime)
# Create the backup file name

# Run the pg_dump command
try:
    print('\a')
    subprocess.run(
        [
            "psql",
            f"--dbname=postgresql://{db_user}:{db_password}@{db_host}:{db_port}/template1",
            "-f" ,latest_backup 
        ],
        check=True
    )
    print(f"Backup successful: {latest_backup}")
except subprocess.CalledProcessError as e:
    print(f"Error during backup: {e}")