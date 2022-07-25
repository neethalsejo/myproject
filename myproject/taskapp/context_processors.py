from django.shortcuts import render
from django.db.models import Q

from .models import Hospital
def menu_links(request):
    links=Hospital.objects.all()
    return dict(links=links)

def doctor(request):
         products = None
         query = None
         if 'branch' in request.GET:
             query = request.GET.get('branch')
             products = Hospital.objects.all().filter(Q(branch__contains=query))
         return render(request, 'appointment.html', {'doctor': query, 'products': products})