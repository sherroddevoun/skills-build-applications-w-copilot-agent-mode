from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {"username": "testuser", "email": "test@example.com", "password": "password123"}

    def test_create_user(self):
        response = self.client.post("/api/users/", self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team_data = {"name": "Team A"}

    def test_create_team(self):
        response = self.client.post("/api/teams/", self.team_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.activity_data = {"user": self.user.id, "type": "Running", "duration": 30, "date": "2025-04-08"}

    def test_create_activity(self):
        response = self.client.post("/api/activities/", self.activity_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Team A")
        self.leaderboard_data = {"team": self.team.id, "points": 100}

    def test_create_leaderboard(self):
        response = self.client.post("/api/leaderboards/", self.leaderboard_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {"name": "Workout A", "description": "Test workout", "duration": 45}

    def test_create_workout(self):
        response = self.client.post("/api/workouts/", self.workout_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
