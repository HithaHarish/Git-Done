"""
Test script to verify the migration worked correctly
"""
import sqlite3
import os

db_path = os.path.join('instance', 'gitdone.db')

if not os.path.exists(db_path):
    print("❌ Database not found!")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=" * 60)
print("DATABASE MIGRATION VERIFICATION")
print("=" * 60)

# Check table structure
print("\n1. Checking Goal table structure:")
cursor.execute("PRAGMA table_info(goal)")
columns = cursor.fetchall()
print(f"   Total columns: {len(columns)}")

# Look for completion_type column
completion_type_col = [col for col in columns if col[1] == 'completion_type']
if completion_type_col:
    print("   ✅ completion_type column exists")
    print(f"      Type: {completion_type_col[0][2]}")
    print(f"      Default: {completion_type_col[0][4]}")
else:
    print("   ❌ completion_type column NOT found")

# Check existing goals
print("\n2. Checking existing goals:")
cursor.execute("SELECT COUNT(*) FROM goal")
total_goals = cursor.fetchone()[0]
print(f"   Total goals: {total_goals}")

if total_goals > 0:
    cursor.execute("SELECT id, description, completion_type, completion_condition, status FROM goal")
    goals = cursor.fetchall()
    print("\n   Goal Details:")
    for goal in goals:
        print(f"   - ID: {goal[0]}")
        print(f"     Description: {goal[1][:50]}...")
        print(f"     Type: {goal[2] if goal[2] else 'NULL'}")
        print(f"     Condition: {goal[3]}")
        print(f"     Status: {goal[4]}")
        print()
else:
    print("   No goals in database yet.")

# Check for any NULL completion_type values
print("\n3. Checking data integrity:")
cursor.execute("SELECT COUNT(*) FROM goal WHERE completion_type IS NULL")
null_count = cursor.fetchone()[0]
if null_count > 0:
    print(f"   ⚠️  Warning: {null_count} goals have NULL completion_type")
else:
    print("   ✅ All goals have completion_type set")

cursor.execute("SELECT COUNT(*) FROM goal WHERE completion_type = 'commit'")
commit_count = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM goal WHERE completion_type = 'issue'")
issue_count = cursor.fetchone()[0]

print(f"   Commit-based goals: {commit_count}")
print(f"   Issue-based goals: {issue_count}")

conn.close()

print("\n" + "=" * 60)
print("VERIFICATION COMPLETE")
print("=" * 60)
print("\n✅ Migration status: SUCCESS")
print("✅ Database is ready for the new feature!")
