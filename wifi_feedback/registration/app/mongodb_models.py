from djongo import models
from django.contrib.auth.models import User

class ComplaintImage(models.Model):
    complaint_id = models.ForeignKey('app.Complaint', on_delete=models.CASCADE, db_constraint=False)
    image = models.ImageField(upload_to='complaint_images/')
    description = models.TextField()

    class Meta:
        db_table = 'complaint_image' # Optional: Set the collection name
        managed = False