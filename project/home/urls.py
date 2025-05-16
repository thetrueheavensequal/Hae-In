from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('doctors/', views.doctors,name='doctors'),
    path('department/', views.department,name='department'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('apply/', views.apply,name='apply'),
    path('status/', views.status,name='status'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.profile, name='profile'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
