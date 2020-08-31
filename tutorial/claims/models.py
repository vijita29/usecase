from django.db import models
from members.models import Members
import datetime

CLAIM_TYPE_CHOICES = (
    ("Medical", "Medical"),
    ("Rx", "Rx"),
    ("Dental", "Dental")
)


# Create your models here.
class Claims(models.Model):
    member_id = models.ForeignKey(Members, related_name='claim', on_delete=models.CASCADE)
    claim_date = models.DateField(default=datetime.date.today)
    billed_amount = models.DecimalField(max_digits=7, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=7, decimal_places=2)
    provider_name = models.CharField(max_length=30)
    claim_type = models.CharField(max_length=20, choices=CLAIM_TYPE_CHOICES)
