from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import AllLayers,Photos,PublicArt,Restaurants,Sports,Testing,WaterLeisure,Zoo
# Register your models here.
admin.site.register(AllLayers,LeafletGeoAdmin)
admin.site.register(Photos)
admin.site.register(PublicArt)
admin.site.register(Restaurants)
admin.site.register(Sports)
admin.site.register(Testing)
admin.site.register(WaterLeisure)
admin.site.register(Zoo)
# admin.site.register(LeafletGeoAdmin)