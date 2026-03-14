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
    pk = models.CompositePrimaryKey('name', 'double_unit')
    name = models.CharField(max_length=5)  # This field type is a guess.
    double_unit = models.BooleanField()  # This field type is a guess.
    diesel = models.BooleanField(null=True)  # This field type is a guess.
    speed = models.IntegerField(null=True)  # This field type is a guess.
    carriages = models.IntegerField(null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'class_table'


class Operator(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=16)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'operator'


class Role(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=16)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'role'


class Player(models.Model):
    username = models.CharField(primary_key=True, unique=True, max_length=20)  # This field type is a guess.
    current_role = models.ForeignKey(Role, db_column='current_role', on_delete=models.SET_DEFAULT, default='passenger')

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
    operator = models.ForeignKey(Operator, db_column='operator', on_delete=models.PROTECT)  # This field type is a guess.
    terminus1 = models.ForeignKey(Station, db_column='terminus1', on_delete=models.CASCADE, related_name="route_terminus1")  # This field type is a guess.
    terminus2 = models.ForeignKey(Station, db_column='terminus2', on_delete=models.CASCADE, related_name="route_terminus2")  # This field type is a guess.
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
    pk = models.CompositePrimaryKey('route', 'stop_order')
    route = models.ForeignKey(Route, on_delete=models.CASCADE)  # This field type is a guess.
    station = models.ForeignKey(Station, on_delete=models.CASCADE)  # This field type is a guess.
    stop_order = models.IntegerField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'stops'


class Unit(models.Model):
    pk = models.CompositePrimaryKey('train_class', 'number')
    train_class = models.TextField(db_column='class')  # hmph.
    double_unit = models.BooleanField()
    number = models.TextField(max_length=2)  # This field type is a guess.
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT)  # This field type is a guess.

    full_class = models.ForeignObject(
        TrainClass,
        on_delete=models.CASCADE,
        from_fields=('train_class', 'double_unit'),
        to_fields=('name', 'double_unit'),
    )

    class Meta:
        managed = False
        db_table = 'unit'


class TrainAssignment(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, unique=True)  # This field type is a guess.
    player = models.ForeignKey(Player, db_column='player', on_delete=models.CASCADE, unique=True)  # This field type is a guess.
    train_class = models.TextField(db_column='class')
    number = models.TextField(db_column='number')
    route = models.ForeignKey(Route, db_column='route', on_delete=models.CASCADE)  # This field type is a guess.
    assign_time = models.TimeField(default=timezone.now())  # This field type is a guess.

    full_unit = models.ForeignObject(
        Unit,
        on_delete=models.CASCADE,
        from_fields=('train_class', 'number'),
        to_fields=('train_class', 'number'),
    )

    class Meta:
        managed = False
        db_table = 'train_assignment'
