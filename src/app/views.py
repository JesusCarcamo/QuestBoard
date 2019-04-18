from django.shortcuts import render
from django.conf import settings

# Create your views here.
def inicio(request):
    return render(request, "base.html")


