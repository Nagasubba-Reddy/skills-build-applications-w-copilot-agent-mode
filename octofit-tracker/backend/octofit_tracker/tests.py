from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass')
        self.assertEqual(user.email, 'spiderman@marvel.com')

    def test_team_creation(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(team.name, 'Avengers')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='spiderman', type='Jumping', duration=10)
        self.assertEqual(activity.type, 'Jumping')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Avengers', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Situps', difficulty='Easy')
        self.assertEqual(workout.name, 'Situps')
