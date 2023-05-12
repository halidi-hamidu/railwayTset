from django.db import models

# Create your models here.
class RailwayModel(models.Model):
    project_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Project list'

    def __str__(self):
        return str(self.project_name)
