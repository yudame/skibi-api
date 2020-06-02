from django.db import models
from simple_history.models import HistoricalRecords
from apps.common.behaviors import Timestampable

BREAKFAST, LUNCH, DINNER, BRUNCH = 'bf', 'ln', 'dn', 'br'
PERIOD_CHOICES = [
    (BREAKFAST, 'breakfast'),
    (LUNCH, 'lunch'),
    (DINNER, 'dinner'),
    (BRUNCH, 'brunch'),
]

class Menu(Timestampable, models.Model):

    shop = models.OneToOneField('shop.Shop', on_delete=models.PROTECT, related_name="menu")

    header_text = models.TextField(default="")
    footer_text = models.TextField(default="")

    # categories - ('thai', 'western', 'italian', 'indian', 'international', 'mediterranean', 'burgers', 'pizza', )

    # SETTINGS
    breakfast_open_time = models.TimeField(null=True, blank=True)
    breakfast_close_time = models.TimeField(null=True, blank=True)
    brunch_open_time = models.TimeField(null=True, blank=True)
    brunch_close_time = models.TimeField(null=True, blank=True)
    lunch_open_time = models.TimeField(null=True, blank=True)
    lunch_close_time = models.TimeField(null=True, blank=True)
    dinner_open_time = models.TimeField(null=True, blank=True)
    dinner_close_time = models.TimeField(null=True, blank=True)


    # HISTORY MANAGER
    history = HistoricalRecords()

    # MODEL PROPERTIES

    # MODEL FUNCTIONS
    def __str__(self):
        return f"{self.shop.name} Menu"


class MenuSection(models.Model):

    name = models.CharField(max_length=50)
    parent = models.ForeignKey('shop.MenuSection', null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.name}"


class CustomMenuSection(models.Model):

    shop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE, related_name='custom_menu_sections')
    name = models.CharField(max_length=50)
    equivalent_menu_section = models.ForeignKey('shop.MenuSection')

    def __str__(self):
        return f"{self.name} ({self.equivalent_menu_section.name})"
