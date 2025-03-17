from django.shortcuts import render
from django.http import HttpResponse

# Example view
def index(request):
    return HttpResponse("Welcome to Sibyl Labs Goal Tracker!")