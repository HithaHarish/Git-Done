import pytest
import os

# Set test environment variables before importing application
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
os.environ['SECRET_KEY'] = 'test-secret-key'
os.environ['BASE_URL'] = 'http://localhost:5000'

from application import application, db

@pytest.fixture(scope='session')
def app():
    """Create and configure a test app instance."""
    # App is already configured with test settings
    test_app = application

    # Create database tables
    with test_app.app_context():
        db.create_all()

    yield test_app

@pytest.fixture(scope='session')
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture(scope='function')
def session(app):
    """Create a new database session for a test."""
    with app.app_context():
        # Start a transaction
        db.session.begin_nested()

        yield db.session

        # Rollback the transaction after the test
        db.session.rollback()