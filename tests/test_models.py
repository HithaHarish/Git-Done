import pytest
from datetime import datetime, timedelta, UTC
from application import Goal

def test_goal_to_dict_required_fields(session):
    """Test Goal.to_dict() with all required fields."""
    # Create a test goal
    deadline = datetime.now(UTC) + timedelta(days=7)
    goal = Goal(
        user_github_id='12345',
        description='Test goal',
        deadline=deadline,
        repo_url='https://github.com/user/repo',
        completion_condition='fix bug',
        status='active',
        repo_owner='user',
        repo_name='repo',
        embed_token='test-token'
    )
    session.add(goal)
    session.commit()

    result = goal.to_dict()

    # Check all expected fields are present
    expected_fields = [
        'id', 'user_github_id', 'description', 'deadline', 'repo_url',
        'completion_condition', 'status', 'created_at', 'embed_token', 'embed_url'
    ]

    for field in expected_fields:
        assert field in result, f"Missing field: {field}"

    # Check data types
    assert isinstance(result['id'], int)
    assert isinstance(result['user_github_id'], str)
    assert isinstance(result['description'], str)
    assert isinstance(result['deadline'], str)
    assert isinstance(result['repo_url'], str)
    assert isinstance(result['completion_condition'], str)
    assert isinstance(result['status'], str)
    assert isinstance(result['created_at'], str)
    assert isinstance(result['embed_token'], str)
    assert isinstance(result['embed_url'], str)

    # Check datetime serialization
    try:
        datetime.fromisoformat(result['deadline'])
        datetime.fromisoformat(result['created_at'])
    except ValueError as e:
        pytest.fail(f"Invalid datetime format: {e}")

    # Check embed_url format
    assert result['embed_url'] == 'http://localhost:5000/embed/test-token'

def test_goal_to_dict_with_completed_at(session):
    """Test Goal.to_dict() with completed_at field."""
    deadline = datetime.now(UTC) + timedelta(days=7)
    completed_at = datetime.now(UTC)
    goal = Goal(
        user_github_id='12345',
        description='Completed goal',
        deadline=deadline,
        repo_url='https://github.com/user/repo',
        completion_condition='fix bug',
        status='completed',
        completed_at=completed_at,
        repo_owner='user',
        repo_name='repo',
        embed_token='test-token-completed'
    )
    session.add(goal)
    session.commit()

    result = goal.to_dict()

    # Check completed_at is serialized
    assert 'completed_at' in result
    assert result['completed_at'] is not None
    assert isinstance(result['completed_at'], str)

    # Check it's valid ISO format
    try:
        datetime.fromisoformat(result['completed_at'])
    except ValueError as e:
        pytest.fail(f"Invalid completed_at datetime format: {e}")

def test_goal_to_dict_without_embed_token(session):
    """Test Goal.to_dict() without embed_token."""
    deadline = datetime.now(UTC) + timedelta(days=7)
    goal = Goal(
        user_github_id='12345',
        description='Goal without embed token',
        deadline=deadline,
        repo_url='https://github.com/user/repo',
        completion_condition='fix bug',
        status='active',
        repo_owner='user',
        repo_name='repo'
    )
    session.add(goal)
    session.commit()

    result = goal.to_dict()

    # Check embed_token and embed_url are None
    assert result['embed_token'] is None
    assert result['embed_url'] is None