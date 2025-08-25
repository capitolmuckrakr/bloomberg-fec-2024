from django.db import models
from django.utils import timezone
from django.db.models import Sum

import datetime

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.__str__()

class Donor(BaseModel):
    bloomberg_name = models.CharField(max_length=255, null=True, blank=True)
    bloomberg_employer = models.CharField(max_length=255, null=True, blank=True)
    bloomberg_occupation = models.CharField(max_length=255, null=True, blank=True)
    bloomberg_note = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    contribution_total_2020 = models.DecimalField(max_digits=12,decimal_places=2, default=0)
    contribution_total_2022 = models.DecimalField(max_digits=12,decimal_places=2, default=0)
    contribution_total_2024 = models.DecimalField(max_digits=12,decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.contribution_total_2022 = self.contributions_2020.filter(active=True).aggregate(Sum('contribution_amount'))['contribution_amount__sum']
        if not self.contribution_total_2020:
            self.contribution_total_2020 = 0
        self.contribution_total_2024 = self.contributions_2022.filter(active=True).aggregate(Sum('contribution_amount'))['contribution_amount__sum']
        if not self.contribution_total_2022:
            self.contribution_total_2022 = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bloomberg_name
