import pytest
import sys
import os
import tempfile

# Add parent directory to path to import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from database import db


@pytest.fixture
def client():
    """Create a test client for the Flask app with in-memory database"""
    # Create a temporary database file
    db_fd, db_path = tempfile.mkstemp()
    
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
    
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def runner():
    """Create a CLI runner for the Flask app"""
    return app.test_cli_runner()


@pytest.fixture
def app_context():
    """Application context for tests"""
    with app.app_context():
        yield app
