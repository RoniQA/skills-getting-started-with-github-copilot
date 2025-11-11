"""Pytest configuration and fixtures for API tests"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities data before each test"""
    # Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Join the school soccer team for practices and matches",
            "schedule": "Tuesdays and Thursdays, 5:00 PM - 7:00 PM",
            "max_participants": 25,
            "participants": ["liam@mergington.edu", "ava@mergington.edu"]
        },
        "Basketball Club": {
            "description": "Pickup games and skill development for basketball players",
            "schedule": "Wednesdays and Fridays, 4:00 PM - 6:00 PM",
            "max_participants": 20,
            "participants": ["noah@mergington.edu", "isabella@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore drawing, painting, and mixed media projects",
            "schedule": "Mondays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["mia@mergington.edu", "charlotte@mergington.edu"]
        },
        "Drama Club": {
            "description": "Acting, stagecraft, and school theater productions",
            "schedule": "Thursdays, 4:00 PM - 6:30 PM",
            "max_participants": 30,
            "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
        },
        "Science Olympiad": {
            "description": "Prepare for science competitions and hands-on challenges",
            "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
            "max_participants": 24,
            "participants": ["lucas@mergington.edu", "grace@mergington.edu"]
        },
        "Debate Team": {
            "description": "Practice argumentation, public speaking, and competitive debates",
            "schedule": "Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 16,
            "participants": ["henry@mergington.edu", "evelyn@mergington.edu"]
        }
    }
    
    # Reset to original state before each test
    activities.clear()
    activities.update(original_activities)
    
    yield
    
    # Clean up after test (reset again)
    activities.clear()
    activities.update(original_activities)
