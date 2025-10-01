"""
Database migration script to add completion_type column to existing goals.
Run this script once to update your existing database.
"""
import sqlite3
import os

# Get database path
db_path = os.path.join('instance', 'gitdone.db')

if not os.path.exists(db_path):
    print(f"Database not found at {db_path}")
    print("No migration needed - database will be created fresh with the new schema.")
    exit(0)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if completion_type column already exists
    cursor.execute("PRAGMA table_info(goal)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'completion_type' in columns:
        print("✓ Migration already applied - completion_type column exists")
    else:
        # Add the completion_type column with default value 'commit'
        print("Adding completion_type column to goal table...")
        cursor.execute("ALTER TABLE goal ADD COLUMN completion_type VARCHAR(20) DEFAULT 'commit' NOT NULL")
        conn.commit()
        print("✓ Migration successful - completion_type column added")
        print("  All existing goals set to 'commit' completion type")
    
    conn.close()
    
except Exception as e:
    print(f"✗ Migration failed: {e}")
    exit(1)
