from django.contrib import admin
from .models import Complaint
from .mongodb_models import ComplaintImage

# Register your models here.
@admin.register(Complaint)

class Complaint(admin.ModelAdmin):
    list_display = ('complaint_id', 'user','complaint_description','room_no','hostel_name', 'verification_status', 'resolution_status')

