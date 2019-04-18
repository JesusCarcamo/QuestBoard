from django.shortcuts import render
from django.conf import settings

# Create your views here.
def inicio(request):
    print("HOLI");
    return render(request, "base.html")

