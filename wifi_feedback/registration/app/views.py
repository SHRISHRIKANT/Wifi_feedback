from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Complaint
from .mongodb_models import ComplaintImage
from django.shortcuts import render, get_object_or_404, redirect
from django.db import router

# Create your views here.

def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same :| ")
        else:
            my_user=User.objects.create_user(username=uname, email=email, password=pass1, first_name=first_name, last_name=last_name)
            my_user.save()
            return redirect('login')
    
    return render (request,'signup.html')

def LoginPage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            if user.is_superuser==True:
                return redirect('c_admin')
            elif user.is_staff==True:
                return redirect('c_warden')
            else:
                return redirect('complaints')
        else:
            return HttpResponse ("Username or Password is incorrect :(" )
        
    return render (request,'login.html')

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def ComplaintPage(request):
    if request.method=='POST':
        
        desc = request.POST.get('complaint_description')
        room = request.POST.get('room_no')
        hostel = request.POST.get('hostel_name')
        
        # Create a new complaint associated with the logged-in user
        user = request.user
        new_complaint = Complaint(user=user, complaint_description=desc, room_no=room, hostel_name=hostel)
        new_complaint.save()
        
        return redirect('display')  # You can redirect to a display page or another appropriate page
    
    return render(request, 'complaints.html')

@login_required(login_url='login')
def AdminPage(request):
    user = request.user
    if user.is_superuser:
        complaints = Complaint.objects.all()
        complaint_images = {}  # Create a dictionary to store image URLs
        for complaint in complaints:
            images = ComplaintImage.objects.using('mongodb').filter(complaint_id=complaint.complaint_id)
            image_urls = [image.image.url for image in images]
            complaint_images[complaint.complaint_id] = image_urls
        return render(request, 'c_admin.html', {'complaints': complaints, 'complaint_images': complaint_images})
    else:
        return HttpResponse("Not authorized")

@login_required(login_url='login')
def WardenPage(request):
    user = request.user
    if user.is_staff:
        complaints = Complaint.objects.all()
        complaint_images = {}  # Create a dictionary to store image URLs
        for complaint in complaints:
            images = ComplaintImage.objects.using('mongodb').filter(complaint_id=complaint.complaint_id)
            image_urls = [image.image.url for image in images]
            complaint_images[complaint.complaint_id] = image_urls
        return render(request, 'c_warden.html', {'complaints': complaints, 'complaint_images': complaint_images})
    else:
        return HttpResponse("Not authorized")

@login_required(login_url='login')
def DisplayPage(request):
    complaints = Complaint.objects.all()
    complaint_images = {}
    for complaint in complaints:
        images = ComplaintImage.objects.using('mongodb').filter(complaint_id=complaint.complaint_id)
        image_urls = [image.image.url for image in images]
        complaint_images[complaint.complaint_id] = image_urls
        
    return render(request, 'display.html', {'complaints': complaints, 'complaint_images': complaint_images})

@login_required(login_url='login')
def change_resolution(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)
    if request.method == 'POST':
        resolution_status = request.POST.get('resolution_status')
        complaint.resolution_status = resolution_status
        complaint.save()
        return redirect('display')
    
    return render(request, 'c_admin.html', {'complaints': Complaint.objects.all()})

@login_required(login_url='login')
def update_all_resolutions(request):
    if request.method == 'POST':
        resolutions = request.POST.dict()
        # Remove CSRF token from the dictionary
        resolutions.pop('csrfmiddlewaretoken', None)
        # Update resolution statuses for all complaints
        for key, resolution_status in resolutions.items():
            if key.startswith('resolution_status_'):
                complaint_id = key.split('_')[2]  # Extract the numeric complaint_id from the key
                complaint = get_object_or_404(Complaint, complaint_id=complaint_id)
                complaint.resolution_status = resolution_status
                complaint.save()
        return redirect('display')
    
    return render(request, 'c_admin.html', {'complaints': Complaint.objects.all()})

@login_required(login_url='login')
def change_verification(request, complaint_id):
    complaint = get_object_or_404(Complaint, complaint_id=complaint_id)
    if request.method == 'POST':
        verification_status = request.POST.get('verification_status')
        complaint.verification_status = verification_status
        complaint.save()
        return redirect('display')
    
    return render(request, 'c_warden.html', {'complaints': Complaint.objects.all()})

@login_required(login_url='login')
def update_all_verifications(request):
    if request.method == 'POST':
        verifications = request.POST.dict()
        # Remove CSRF token from the dictionary
        verifications.pop('csrfmiddlewaretoken', None)
        # Update resolution statuses for all complaints
        for key, verification_status in verifications.items():
            if key.startswith('verification_status_'):
                complaint_id = key.split('_')[2]  # Extract the numeric complaint_id from the key
                complaint = get_object_or_404(Complaint, complaint_id=complaint_id)
                complaint.verification_status = verification_status
                complaint.save()
        return redirect('display')
    
    return render(request, 'c_warden.html', {'complaints': Complaint.objects.all()})

@login_required(login_url='login')
def ComplaintPage(request):
    if request.method == 'POST':
        desc = request.POST.get('complaint_description')
        room = request.POST.get('room_no')
        hostel = request.POST.get('hostel_name')
        image = request.FILES.get('image')
        image_description = request.POST.get('image_description')  # Get the image description

        # Create a new complaint associated with the logged-in user
        user = request.user
        new_complaint = Complaint(user=user, complaint_description=desc, room_no=room, hostel_name=hostel)
        new_complaint.save()

        # Create a new ComplaintImage object associated with the complaint
        complaint_image = ComplaintImage(complaint_id=new_complaint,image=image, description=image_description)
        complaint_image.save()
        
        return redirect('display')  # Redirect to a display page or another appropriate page

    return render(request, 'complaints.html')


def delete_complaint(request, complaint_id):
    if request.method == 'POST':
        # Get the complaint object to be deleted
        complaint_to_delete = Complaint.objects.get(pk=complaint_id)
        c_i = ComplaintImage.objects.get(pk=complaint_id)

        # Retrieve and delete associated complaint images
        complaint_images = ComplaintImage.objects.filter(complaint_id=complaint_to_delete.complaint_id)
        for image in complaint_images:
            image.image.delete()  # Delete the image file
            image.delete()  # Delete the ComplaintImage object

        # Delete the complaint itself
        complaint_to_delete.delete()
        c_i.delete()

        return redirect('display')  # Redirect to a display page or another appropriate page
    
    images = ComplaintImage.objects.using('mongodb').filter(complaint_id=complaint_id)
    image_urls = [image.image.url for image in images]

    complaints = Complaint.objects.all()
    complaint_images = {}

    for complaint in complaints:
        images = ComplaintImage.objects.using('mongodb').filter(complaint_id=complaint.complaint_id)
        image_urls = [image.image.url for image in images]
        complaint_images[complaint.complaint_id] = image_urls

    return render(request, 'delete_complaint.html', {'complaints': complaints, 'complaint_images': complaint_images})
