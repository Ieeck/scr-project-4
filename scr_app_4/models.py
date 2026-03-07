# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Class(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    double_unit = models.TextField(blank=True, null=True)  # This field type is a guess.
    diesel = models.TextField(blank=True, null=True)  # This field type is a guess.
    speed = models.TextField(blank=True, null=True)  # This field type is a guess.
    carriages = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'class'


class Operator(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'operator'


class Player(models.Model):
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_role = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'player'


class Role(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'role'


class Route(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    terminus1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    terminus2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    diesel = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'route'


class Station(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    platforms = models.TextField(blank=True, null=True)  # This field type is a guess.
    dispatchers = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'station'


class StationAssignment(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    player = models.TextField(blank=True, null=True)  # This field type is a guess.
    station = models.TextField(blank=True, null=True)  # This field type is a guess.
    assign_time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'station_assignment'


class Stops(models.Model):
    route = models.TextField(blank=True, null=True)  # This field type is a guess.
    station = models.TextField(blank=True, null=True)  # This field type is a guess.
    stop_order = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'stops'


class TrainAssignment(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    player = models.TextField(blank=True, null=True)  # This field type is a guess.
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word. This field type is a guess.
    number = models.TextField(blank=True, null=True)  # This field type is a guess.
    route = models.TextField(blank=True, null=True)  # This field type is a guess.
    assign_time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'train_assignment'


class Unit(models.Model):
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word. This field type is a guess.
    double_unit = models.TextField(blank=True, null=True)  # This field type is a guess.
    number = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'unit'