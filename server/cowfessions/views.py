from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import util

# Models
from .models import Cowfession

# Create your views here.

def index(request):
    pass