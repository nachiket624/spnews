from django.shortcuts import render, get_object_or_404
from adminpage.models import draft, herosection, herosectionnews, AdvertisementManger
from django.db.models import Q
# Create your views here.


def index(request):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    return render(request,"index.html",{"newnews":draft.objects.all(),"hero":herosection.objects.first(),"NHero":herosectionnews.objects.all()})
=======
    return render(request,"index.html",{"newnews":draft.objects.all(),"hero":herosection.objects.all(),"NHero":herosectionnews.objects.all()})
>>>>>>> Stashed changes
=======
    return render(request, "index.html", {"newnews": draft.objects.all(), "hero": herosection.objects.first(), "NHero": herosectionnews.objects.all(),'newspagead': AdvertisementManger.objects.filter(topage=0)})
>>>>>>> Stashed changes


def news(request, id):
    show = get_object_or_404(draft, pk=id)
    return render(request, 'news.html', {'show': draft.objects.filter(id=id), "share": draft.objects.filter(id=id).only('newstitle', 'newsthumbnail')})

def bigcard(request, id):
    show=get_object_or_404(draft, pk=id)
    return render(request, 'herosectionnews.html', {'hnews': herosection.objects.filter(id=id)})
def herosectionnewscard(request, id):
    show=get_object_or_404(draft, pk=id)
    return render(request, 'livepage.html', {'hnewscard': herosectionnews.objects.filter(id=id)})

def commingsoon(request):
    return render(request, 'commingsoon.html')
