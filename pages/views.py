from django.shortcuts import render
from listings.models import Listings
from realtors.models import Realtor 
def index(request):
    listings=Listings.objects.all().order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings
    }
    return render(request,'pages/index.html',context)
def about(request):
    realtor=Realtor.objects.all()
    mvp_realtor=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtor,
        'mvp_realtors': mvp_realtor
    }
    return render(request,'pages/about.html',context)
    