# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.gis.geos import GEOSGeometry  
from django.contrib.gis.db import models
from decimal import Decimal


class AllLayers(models.Model):
    geoid = models.SmallIntegerField(primary_key=True)
    place_name = models.CharField(max_length=128, blank=True, null=True)
    icon_name = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_layers'

class PublicArt(models.Model):
    geoid = models.SmallIntegerField(primary_key=True, blank=True, null=False)
    park_name = models.CharField(max_length=128, blank=True, null=True)
    park_number = models.SmallIntegerField(blank=True, null=True)
    place_name = models.CharField(max_length=128, blank=True, null=True)
    artist_name = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geom = models.PointField("POINT({0} {1})".format(longitude, latitude))
    # geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    # latitude = Decimal(59.32932)  
    # longitude = Decimal(18.06858)
    # geom = GEOSGeometry("POINT({0} {1})".format(longitude, latitude))

    def __unicode__(self):
        return self.geoid

    class Meta:
        managed = False
        db_table = 'public_art'

class Photos(models.Model):
    ids = models.CharField(primary_key=True,max_length=128, editable=False)
    caption = models.CharField(max_length=128)
    image = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    
    # @property
    # def popupContent(self):
    #   return '<img src="/Users/sig/Desktop/project_2_park_app/images/{}" >'.format(
    #       self.image.url
          # )
# // popUpContent += "<img src='/Users/sig/Desktop/project_2_park_app/images/" +feature.properties["image"]+ "'>";
    class Meta:
        managed = False
        db_table = 'photos'


class Restaurants(models.Model):
    geoid = models.SmallIntegerField(primary_key=True,blank=True, null=False)
    activity_type = models.CharField(max_length=128, blank=True, null=True)
    place_name = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geom = models.PointField("POINT({0} {1})".format(longitude, latitude))

    class Meta:
        managed = False
        db_table = 'restaurants'


class Sports(models.Model):
    geoid = models.SmallIntegerField(primary_key=True,blank=True, null=False)
    place_name = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geom = models.PointField("POINT({0} {1})".format(longitude, latitude))

    class Meta:
        managed = False
        db_table = 'sports'


class WaterLeisure(models.Model):
    geoid = models.SmallIntegerField(primary_key=True)
    activity_type = models.CharField(max_length=128, blank=True, null=False)
    place_name = models.CharField(max_length=128, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom = models.PointField("POINT({0} {1})".format(longitude, latitude))

    class Meta:
        managed = False
        db_table = 'water_leisure'

class Testing(models.Model):
    person_name = models.CharField(primary_key=True,max_length=128)

    class Meta:
        managed = False
        db_table = 'testing'

class Zoo(models.Model):
    geoid = models.SmallIntegerField(primary_key=True)
    activity_type = models.CharField(max_length=128, blank=True, null=True)
    place_name = models.CharField(max_length=128, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    geom = models.PointField("POINT({0} {1})".format(longitude, latitude))

    class Meta:
        managed = False
        db_table = 'zoo'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'
