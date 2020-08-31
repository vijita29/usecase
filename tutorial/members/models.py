from django.db import models
import uuid


# Create your models here.
class Members(models.Model):
    # member_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    member_name = models.CharField(max_length=30)
