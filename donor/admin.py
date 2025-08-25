from django.contrib import admin
from donor.models import *

class DonorAdmin(admin.ModelAdmin):
    search_fields = ['bloomberg_name']
    ordering = ('bloomberg_name',)
    list_display = ('bloomberg_name','contribution_total_2024','contribution_total_2022','contribution_total_2020')

admin.site.register(Donor, DonorAdmin)
