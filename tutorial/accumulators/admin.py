from django.contrib import admin
from .models import Accumulator

# Register your models here.
@admin.register(Accumulator)
class AccumulatorAdmin(admin.ModelAdmin):
    pass