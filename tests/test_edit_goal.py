import json
import pytest
from application import application, db, User, Goal

@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test.db"
    application.config['TESTING'] = True
    application.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    with application.app_context():
        db.create_all()
        yield application.test_client()
        db.session.remove()
        db.drop_all()


def test_create_and_update_goal(client):
    # create user
    with application.app_context():
        user = User(github_id='test123', username='tester', access_token='tok')
        db.session.add(user)
        db.session.commit()

    # set session (login)
    with client.session_transaction() as sess:
        sess['user_github_id'] = 'test123'
        sess['username'] = 'tester'

    # create a goal
    create_payload = {
        "description": "Initial goal",
        "deadline": "12/12/2025 23:59",
        "deadline_display": "12/12/2025 23:59",
        "repo_url": "https://github.com/owner/repo",
        "completion_condition": "#done",
        "completion_type": "commit"
    }
    res = client.post("/api/goals", data=json.dumps(create_payload), content_type='application/json')
    assert res.status_code == 201
    data = res.get_json()
    goal_id = data['id']

    # update the goal
    update_payload = {
        "description": "Edited goal",
        "deadline": "13/12/2025 23:59",
        "deadline_display": "13/12/2025 23:59"
    }
    res2 = client.put(f"/api/goals/{goal_id}", data=json.dumps(update_payload), content_type='application/json')
    assert res2.status_code == 200
    updated = res2.get_json()
    assert updated['description'] == "Edited goal"
    assert updated['deadline_display'] == "13/12/2025 23:59"
