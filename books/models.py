# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class book(models.Model):                    # model - class    - table
    name = models.CharField(max_length=255)  # field - instance - row

  
    def __str__(self):
        return self.name
