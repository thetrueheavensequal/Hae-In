from django.db import models
from django.contrib.auth.models import User
from . import *
# Create your models here.
class Departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()
    def __str__(self):
        return self.dept_name
    class Meta:
        verbose_name_plural = 'Departments'

        
class Doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doc_name
    def __str__(self):
        return f"{self.doc_name} ({self.doc_spec})"
    class Meta:
        verbose_name_plural = 'Doctors'

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    appmnt_date = models.DateField()
    appmnt_on = models.DateField(auto_now=True)  # Auto-updated field (not needed in form)

    def __str__(self):
        return f"{self.doc_name.doc_name} - {self.doc_name.doc_spec}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
