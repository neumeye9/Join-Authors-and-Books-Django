# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Authors(models.Model):
    first_name =models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Books(models.Model):
    title = models.TextField()
    published_date = models.DateField('%m/%d/%Y')
    category=models.CharField(max_length=50)
    in_print=models.BooleanField()
    author =models.ForeignKey(Authors)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)