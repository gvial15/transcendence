# script to reset the DB

import os
import django
from django.db import connection
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transcendence.settings')
django.setup()

def empty_database():
    with connection.cursor() as cursor:
        cursor.execute("DROP SCHEMA public CASCADE;")
        cursor.execute("CREATE SCHEMA public;")
        print("Database emptied.")

    # Reapply migrations to recreate the database schema
    call_command('migrate')

if __name__ == "__main__":
    confirm = input("Are you sure you want to empty the database? This cannot be undone. Type 'yes' to confirm: ")
    if confirm.lower() == 'yes':
        empty_database()
        print("Database schema recreated.")
    else:
        print("Operation cancelled.")

# run with: docker-compose exec web python /code/reset_db.py