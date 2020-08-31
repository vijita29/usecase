from django.db import models
from members.models import Members

# Create your models here.
class Accumulator(models.Model):
    member_id = models.ForeignKey(Members, related_name='accumulator', on_delete=models.CASCADE)
    ind_deduct_limit = models.DecimalField(max_digits=5, decimal_places=2)
    ind_deduct_used = models.DecimalField(max_digits=5, decimal_places=2)
    ind_ofp_limit = models.DecimalField(max_digits=5, decimal_places=2)
    ind_ofp_used = models.DecimalField(max_digits=5, decimal_places=2)
    family_deduct_limit = models.DecimalField(max_digits=5, decimal_places=2)
    family_deduct_used = models.DecimalField(max_digits=5, decimal_places=2)
    family_ofp_limit = models.DecimalField(max_digits=5, decimal_places=2)
    family_ofp_used = models.DecimalField(max_digits=5, decimal_places=2)
