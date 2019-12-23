from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import *

class Summary(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()
    word_count = models.PositiveIntegerField()
    date = models.DateTimeField(default=datetime.now)
    processed_language = models.CharField(max_length = 2)
    json_response = models.TextField(default="")
    tipo = models.PositiveIntegerField(default=1) #1 = twiiter #2 = texto

class Pillar(models.Model):
    name = models.CharField(max_length = 50)
    pillar_id = models.CharField(max_length = 50)
    def __str__(self):
        return "{0}".format(self.name)

class Category(models.Model):
    pillar = models.ForeignKey(Pillar, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50)
    significant = models.BooleanField()
    trait_id = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    significant = models.BooleanField()
    trait_id = models.CharField(max_length = 100)

class CategoryResult(models.Model):
    summary = models.ForeignKey(Summary, on_delete = models.CASCADE, default = None)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    percentile = models.DecimalField(max_digits = 16, decimal_places = 2)
    raw_score = models.DecimalField(max_digits = 16, decimal_places = 2)

class SubCategoryResult(models.Model):
    summary = models.ForeignKey(Summary, on_delete = models.CASCADE, default = None)
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    percentile = models.DecimalField(max_digits = 16, decimal_places = 2)
    raw_score = models.DecimalField(max_digits = 16, decimal_places = 2)
