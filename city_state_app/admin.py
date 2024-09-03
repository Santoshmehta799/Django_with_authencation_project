from django.contrib import admin
from city_state_app import models
# Register your models here.
@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id','name','state_code', 'country_name')
    list_filter  =['country__name']
    def country_name(self,obj):
        return obj.country.name

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state_name')
    search_fields = ['state__name', "name"]
    list_filter  =['state__name']

    def state_name(self,obj):
        return obj.state.name