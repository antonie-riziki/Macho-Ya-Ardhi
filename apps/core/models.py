from django.db import models
from django.conf import settings

class LandParcel(models.Model):
    parcel_number = models.CharField(max_length=100, unique=True)
    title_number = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255)
    acreage = models.FloatField(blank=True, null=True)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parcel_number

class TransactionCase(models.Model):
    RISK_LEVELS = [
        ('LOW', 'Low Risk'),
        ('MEDIUM', 'Medium Risk'),
        ('HIGH', 'High Risk'),
        ('CRITICAL', 'Critical Risk'),
    ]
    
    parcel = models.ForeignKey(LandParcel, on_delete=models.CASCADE, related_name='cases')
    buyer_name = models.CharField(max_length=255)
    risk_score = models.CharField(max_length=10, choices=RISK_LEVELS, default='MEDIUM')
    summary = models.TextField()
    report_file = models.FileField(upload_to='reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Case: {self.parcel.parcel_number} - {self.risk_score}"

class FraudReport(models.Model):
    reporter_phone = models.CharField(max_length=20)
    parcel_number = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    is_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.reporter_phone} at {self.created_at}"
