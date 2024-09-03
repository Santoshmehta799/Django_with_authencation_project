from django.db import models
import uuid
from auth_app_user.models import ModelMixin
from django.utils.translation import gettext_lazy as _ 

# Create your models here.

class Country(ModelMixin):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
   name = models.CharField(max_length=255, null=True, blank=True)

   def __str__(self) -> str:
       return f"{self.name}"
   
   class Meta:
        verbose_name = _("City State Model - Country")
        verbose_name_plural = _('City State Model - Country')


class State(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='state')
    state_code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
       return f"{self.name}"
    
    class Meta:
        verbose_name = _("City State Model - State")
        verbose_name_plural = _('City State Model - State')


class City(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='city')
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
       return f"{self.name}"
    
    class Meta:
        verbose_name = _('App Model - Category')
        verbose_name_plural = _('App Model - Category')
    
    class Meta:
        verbose_name = _("City State Model - City")
        verbose_name_plural = _('City State Model - City')

