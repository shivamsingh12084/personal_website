from django.forms import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ConsultationForm, ContactForm, DetailedContactForm
from django.contrib import messages
# Create your views here.


class HomePageView(FormView):
    form_class = ConsultationForm
    template_name = 'home.html'
    success_url = 'http://127.0.0.1:8000'

    def form_valid(self, form):
        subject = "About consultation"
        from_email = form.cleaned_data['senders_email']
        message = "I want you consultation, Please contact me as early as possible"
        send_mail(subject, message, from_email, ['shivamsingh12084@gmail.com'])
        messages.success(self.request, 'Thanks for booking I will get back to you')
        return super().form_valid(form)


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PortfolioPageView(TemplateView):
    template_name = 'portfolio.html'


class BlogPageView(TemplateView):
    template_name = 'blog.html'


class ContactPageView(FormView):
    form_class = DetailedContactForm
    template_name = 'contact.html'
    success_url = '/contact'

    def form_valid(self , form):
        subject = form.cleaned_data['subject']
        from_email = form.cleaned_data['from_email']
        message = form.cleaned_data['detailed_message']
        send_mail(subject, message, from_email, ['shivamsingh@gmail.com'])
        messages.success(self.request, 'Contact request submitted successfully.')
        return super().form_valid(form)
        
        





def successView(request):
    return HttpResponse('Sucess Thank you for your message.')
