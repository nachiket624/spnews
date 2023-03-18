from django.shortcuts import render
from adminpage.models import draft

# Create your views here.
def index(request):
    return render(request,"index.html",{"newnews":draft.objects.all()})

def news(request):
    return render(request,"news.html")