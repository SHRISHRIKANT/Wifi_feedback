"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('complaints/',views.ComplaintPage,name='complaints'),
    path('c_admin/',views.AdminPage,name='c_admin'),
    path('c_warden/',views.WardenPage,name='c_warden'),
    path('display/',views.DisplayPage,name='display'),
    path('change_resolution/<int:complaint_id>/', views.change_resolution, name='change_resolution'),
    path('change_verification/<int:complaint_id>/', views.change_verification, name='change_verification'),
    path('update_all_resolutions/', views.update_all_resolutions, name='update_all_resolutions'),
    path('update_all_verifications/', views.update_all_verifications, name='update_all_verifications'),
    path('logout/',views.LogoutPage,name='logout'),
    path('delete_complaint/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
