from django.shortcuts import render
from . models import Listings

# Create your views here.
def index(request):
    listings=Listings.objects.all()
    context={
        'listings':listings
    }
    return render(request, 'listings/listings.html',context)
def listing(request):
    return render(request, 'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')
       
