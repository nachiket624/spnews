from django.shortcuts import render,get_object_or_404
from adminpage.models import draft

# Create your views here.
def index(request):
    return render(request,"index.html",{"newnews":draft.objects.all()})

def news(request,id) :
    show = get_object_or_404(draft, pk=id)
    return render(request, 'news.html',{'show':draft.objects.filter(id=id)})