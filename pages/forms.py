from tkinter import W
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email@gmail.com', 'class': 'form-control rounded'}) ,required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control rounded'}) ,required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control', 'rows': '5'}), required=True)


class ConsultationForm(forms.Form):
    senders_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email@gmail.com', 'class': 'form-control rounded'}) ,required=True)


class DetailedContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'contactName', 'type': 'text', 'placeholder': 'username@email.com'}) ,required= True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'contactName', 'type': 'text', 'placeholder': 'Subject'}) ,required=True)
    detailed_message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'contactMessage', 'rows': '5', 'placeholder':'Tell me what i can help you with!'}), required=True)