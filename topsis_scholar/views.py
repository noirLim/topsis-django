from django.shortcuts import render

def index_home(request):
    return render(request,"index.html")