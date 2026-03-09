# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone


class TrainClass(models.Model):
    name = models.TextField(primary_key=True, max_length=5)  # This field type is a guess.
    double_unit = models.BooleanField(primary_key=True)  # This field type is a guess.
    diesel = models.BooleanField(null=True)  # This field type is a guess.
    speed = models.IntegerField(null=True)  # This field type is a guess.
    carriages = models.IntegerField(null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'class_table'


class Operator(models.Model):
    name = models.TextField(primary_key=True, unique=True, max_length=16)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'operator'


class Role(models.Model):
    name = models.TextField(primary_key=True, unique=True, max_length=16)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'role'


class Player(models.Model):
    username = models.TextField(primary_key=True, unique=True, max_length=20)  # This field type is a guess.
    current_role = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, default='passenger')

    class Meta:
        managed = False
        db_table = 'player'


class Station(models.Model):
    name = models.TextField(primary_key=True, max_length=64)  # This field type is a guess.
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT)  # This field type is a guess.
    platforms = models.IntegerField(null=True)  # This field type is a guess.
    dispatchers = models.IntegerField(null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'station'


class Route(models.Model):
    id = models.TextField(primary_key=True, unique=True, max_length=3)  # This field type is a guess.
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT)  # This field type is a guess.
    terminus1 = models.ForeignKey(Station, on_delete=models.CASCADE)  # This field type is a guess.
    terminus2 = models.ForeignKey(Station, on_delete=models.CASCADE)  # This field type is a guess.
    diesel = models.BooleanField(null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'route'


class StationAssignment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)  # This field type is a guess.
    player = models.ForeignKey(Player, on_delete=models.CASCADE, unique=True)  # This field type is a guess.
    station = models.ForeignKey(Station, on_delete=models.CASCADE)  # This field type is a guess.
    assign_time = models.TimeField(default=timezone.now())  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'station_assignment'


class Stops(models.Model):
    route = models.ForeignKey(Route, primary_key=True, on_delete=models.CASCADE)  # This field type is a guess.
    station = models.ForeignKey(Station, on_delete=models.CASCADE)  # This field type is a guess.
    stop_order = models.IntegerField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'stops'


class Unit(models.Model):
    train_class = models.ForeignKey(TrainClass, db_column='class', primary_key=True, on_delete=models.CASCADE)  # Field renamed because it was a Python reserved word. This field type is a guess.
    double_unit = models.ForeignKey(TrainClass, on_delete=models.CASCADE)  # This field type is a guess.
    number = models.TextField(primary_key=True, max_length=2)  # This field type is a guess.
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'unit'


class TrainAssignment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)  # This field type is a guess.
    player = models.ForeignKey(Player, on_delete=models.CASCADE, unique=True)  # This field type is a guess.
    train_class = models.ForeignKey(Unit, on_delete=models.CASCADE)  # Field renamed because it was a Python reserved word. This field type is a guess.
    number = models.ForeignKey(Unit, on_delete=models.CASCADE)  # This field type is a guess.
    route = models.ForeignKey(Route, on_delete=models.CASCADE)  # This field type is a guess.
    assign_time = models.TimeField(default=timezone.now())  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'train_assignment'
