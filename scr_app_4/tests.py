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
        test_role = Role.objects.create(name='role')
        test_player = Player.objects.create(username='test', current_role=test_role)
        test_player.delete()

    def test_create_delete_assignment(self):
        test_role = Role.objects.create(name='role')
        test_operator = Operator.objects.create(name='operator')
        test_station = Station.objects.create(name='station', operator=test_operator)
        test_player = Player.objects.create(username='test', current_role=test_role)
        test_class = TrainClass.objects.create(name='185/1', double_unit=0)
        test_unit = Unit.objects.create(train_class=test_class, double_unit=0, number='01', operator=test_operator)
        test_route = Route.objects.create(id='001', operator=test_operator, terminus1=test_station, terminus2=test_station)

        assignment = TrainAssignment.objects.create(
            player=test_player,
            train_class=test_class,
            number=test_unit.number,
            route=test_route
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