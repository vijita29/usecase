from django.contrib import admin
from .models import Claims

# Register your models here.
@admin.register(Claims)
class ClaimsAdmin(admin.ModelAdmin):
    pass