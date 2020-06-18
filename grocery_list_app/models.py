import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class GroceryItem(models.Model):
  text_description = models.CharField(max_length=200)
  created_date = models.DateTimeField()
  completed_date = models.DateTimeField(null=True, blank=True)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.text_description



# a model called GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed