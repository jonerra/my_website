from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class MessageCreateView(CreateView):
    model = Message
    template_name = "contact/message_form.html"
    fields = ['subject', 'name', 'email', 'message']
    success_url = reverse_lazy('success')

class Success(TemplateView):
    template_name = "success.html"

class About(TemplateView):
    template_name = "contact/about_me_form.html"
    
class Resume(TemplateView):
    template_name = "contact/resume.html"