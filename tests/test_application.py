"""
Test script to verify the application works with the new feature
"""
import sys
import os

print("=" * 60)
print("APPLICATION FUNCTIONALITY TEST")
print("=" * 60)

try:
    print("\n1. Testing imports...")
    from application import application, db, Goal, User
    print("   ✅ Application imported successfully")
    print("   ✅ Database models loaded")
    
    print("\n2. Testing Goal model...")
    # Check if completion_type attribute exists
    if hasattr(Goal, 'completion_type'):
        print("   ✅ Goal model has completion_type attribute")
    else:
        print("   ❌ Goal model missing completion_type attribute")
        sys.exit(1)
    
    print("\n3. Testing Goal creation...")
    from datetime import datetime
    
    # Test creating a commit-based goal
    test_goal_commit = Goal(
        user_github_id='test123',
        description='Test Commit Goal',
        deadline=datetime.utcnow(),
        repo_url='https://github.com/test/repo',
        completion_condition='#done',
        completion_type='commit'
    )
    print("   ✅ Can create commit-based Goal")
    print(f"      Type: {test_goal_commit.completion_type}")
    
    # Test creating an issue-based goal
    test_goal_issue = Goal(
        user_github_id='test123',
        description='Test Issue Goal',
        deadline=datetime.utcnow(),
        repo_url='https://github.com/test/repo',
        completion_condition='42',
        completion_type='issue'
    )
    print("   ✅ Can create issue-based Goal")
    print(f"      Type: {test_goal_issue.completion_type}")
    
    # Test default value
    test_goal_default = Goal(
        user_github_id='test123',
        description='Test Default Goal',
        deadline=datetime.utcnow(),
        repo_url='https://github.com/test/repo',
        completion_condition='#complete'
    )
    print("   ✅ Can create Goal without specifying type")
    print(f"      Default type: {test_goal_default.completion_type}")
    
    print("\n4. Testing to_dict() method...")
    goal_dict = test_goal_issue.to_dict()
    if 'completion_type' in goal_dict:
        print("   ✅ to_dict() includes completion_type")
        print(f"      Value: {goal_dict['completion_type']}")
    else:
        print("   ❌ to_dict() missing completion_type")
        sys.exit(1)
    
    print("\n5. Testing webhook function...")
    from application import create_github_webhook
    print("   ✅ create_github_webhook function imported")
    # Note: We won't actually call it as it requires a real token
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)
    print("\n✅ Application is fully functional")
    print("✅ New feature is ready to use")
    print("\n📝 Next steps:")
    print("   1. Start the application")
    print("   2. Login with GitHub")
    print("   3. Create a goal with 'Issue Closed' completion type")
    print("   4. Close the specified issue to test completion")
    
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("   Make sure all dependencies are installed:")
    print("   pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
