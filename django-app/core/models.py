from django.db import models


class Article(models.Model):
    headline = models.TextField(null=False)
    content = models.TextField(null=False)
