from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_id = models.AutoField(primary_key=True)  # Automatically generated complaint ID
    complaint_description = models.TextField()
    room_no = models.TextField()
    hostel_name = models.TextField()
    
    # Define choices for verification status
    VERIFICATION_CHOICES = (
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('not_verified', 'Not Verified'),
    )
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_CHOICES, default='pending')
    
    # Define choices for resolution status
    RESOLUTION_CHOICES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
        ('not_resolved', 'Not Resolved'),
    )
    resolution_status = models.CharField(max_length=20, choices=RESOLUTION_CHOICES, default='pending')
    
    def __str__(self):
        return f"Complaint ID: {self.complaint_id} by {self.user.username}"

