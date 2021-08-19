from django.urls import path
from . import views 

urlpatterns=[
    path('',views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'), #used to capture integer value clicked in listings table (URL mese catch krne ke liye <>)
    path('search', views.search, name='searchlisting')  
]