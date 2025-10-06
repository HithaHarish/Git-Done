import json
from datetime import datetime

def test_health_endpoint(client):
    """Test the /api/health endpoint returns healthy status."""
    response = client.get('/api/health')

    # Check status code
    assert response.status_code == 200

    # Parse JSON response
    data = json.loads(response.data)

    # Check required fields are present
    assert 'status' in data
    assert 'timestamp' in data
    assert 'service' in data

    # Check status is healthy
    assert data['status'] == 'healthy'

    # Check service name
    assert data['service'] == 'git-done-api'

    # Check timestamp is valid ISO format
    try:
        datetime.fromisoformat(data['timestamp'])
    except ValueError:
        pytest.fail("Timestamp is not in valid ISO format")