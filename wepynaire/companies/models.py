from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "companies"


class Project(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("share_project", "can share the project with others"),
            ("close_project", "can close the project"),
        ]
