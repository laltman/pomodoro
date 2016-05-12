from django.db import models
from django.core.validators import MinValueValidator
import datetime

# Create your models here.
PRIORITY_CHOICES = ( 

  (1, 'Low'), 

  (2, 'Normal'), 

  (3, 'High'), 

)


class Task(models.Model): 

  title = models.CharField(max_length=250, unique=True)

  created_date = models.DateTimeField(default=datetime.datetime.now) 

  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 

  pomnumber = models.IntegerField(default=1, validators=[MinValueValidator(1)])

  def __str__(self): 

    return self.title 

  class Meta: 

    ordering = ['-priority', 'title']  

  class Admin: 

    pass


