from django.test import TestCase
from .models import *

class TestClass(TestCase):
    def test_get_everything(self):
        TrainClass.objects.all()
        Operator.objects.all()
        Role.objects.all()
        Player.objects.all()
        Station.objects.all()
        Route.objects.all()
        StationAssignment.objects.all()
        Route.objects.all()
        Unit.objects.all()
        TrainAssignment.objects.all()

    def test_create_delete_player(self):
        test_role = Role.objects.get(name='passenger')
        test_player = Player.objects.create(username='test', current_role=test_role)
        test_player.delete()

    def test_create_delete_assignment(self):
        player = Player.objects.get(username='leeck_reflexive')
        train_class = TrainClass.objects.get(name='185/1')
        unit = Unit.objects.get(number='45')
        route = Route.objects.get(id='051')

        assignment = TrainAssignment.objects.create(
            player=player,
            train_class=train_class,
            unit=unit,
            route=route
        )
        assignment.delete()

    # page tests

    def test_players_page(self):
        response = self.client.get("/players/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "players.html")

    def test_assignments_page(self):
        response = self.client.get("/assignments/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "assignments.html")

    def test_create_player_page(self):
        response = self.client.get("/create_player/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_player.html")

    def test_create_assignments_page(self):
        response = self.client.get("/create_assignment/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_assignment.html")