from django.db import models

# Create your models here.
class Participant(models.Model):
    reg_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    org_name = models.CharField(max_length=256)
    # still more to come.
    def __str__(self):
        return self.name
