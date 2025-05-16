from django import forms
from django.contrib.auth.models import User
from . models import Appointment, ContactMessage

class DateInput(forms.DateTimeInput):
    input_type = 'date'
class AppmntForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'appmnt_date' : DateInput
            }
        labels = {
            'p_name' : 'Patient Full Name',
            'p_phone' : 'Phone Number',
            'p_email' : 'Email Address',
            'doc_name' : 'Doctor Name',
            'appmnt_date' : 'Appointment Date',
            'appmnt_on' : 'Appointment On :'
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }