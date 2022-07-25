from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Patient,Hospital
from django.db.models import Q
from django.http import JsonResponse,HttpResponseBadRequest
import json
# Create your views here.
def detail(request,c_slug=None):
    c_page = None
    hospital_list = None
    if c_slug != None:
        c_page = get_object_or_404(Hospital, slug=c_slug)
        hospital_list = Hospital.objects.all().filter(branch=c_page, available=True)
    else:
        hospital_list = Hospital.objects.all().filter(available=True)

    return render(request, "hospitaldetails.html",{'category': c_page,'hospital_list':hospital_list})


def appointment(request, patient_slug, c_slug):
    try:
        hospital_list = Hospital.objects.get(category__slug=c_slug, slug=patient_slug)
    except Exception as e:
        raise e
    return render(request, 'appointment.html', {'product': hospital_list})
    return render(request,"appointment.html")

def RegDetail(request,c_slug=None):
    c_page = None
    hospital_list = None
    if c_slug != None:
        c_page = get_object_or_404(Hospital)
        hospital_list = Hospital.objects.all().filter(branch=c_page, available=True)
    else:
        hospital_list = Hospital.objects.all().filter(available=True)

    return render(request, "appointment.html",{'category': c_page,'hospital_list':hospital_list})


def appointment(request):
    if request.method=="POST":
        username=request.POST.get('username',)
        pname=request.POST.get('pname',)
        slug=request.POST.get('pname',)
        age = request.POST.get('age',)
        gender = request.POST.get('gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        branch = request.POST.get('branch', )
        diseas = request.POST.get('diseas', )
        dname = request.POST.get('dname', )
        appdate = request.POST.get('appdate', )
        patient=Patient(username=username,pname=pname,slug=slug,age=age,gender=gender,phone=phone,email=email,address=address,branch=branch,diseas=diseas,dname=dname,appdate=appdate)
        patient.save()

        return render(request, 'confirm.html', {'task1':patient})


def ajaxq(request):
        bid = request.GET.get('bid')
        hospital = Hospital.objects.get(pk=bid)
        return JsonResponse({'pediatrician':hospital.pediatrician, 'urologist':hospital.urologist, 'physician':hospital.physician,'gynaecologist':hospital.gynaecologist, 'ent':hospital.ent})


def doctor(request):
        products = None
        query = None
        if 'branch' in request.GET:
             query = request.GET.get('branch')
             products = Hospital.objects.all().filter(branch__contains=query)

        return render(request, 'appointment.html', {'doctor': query, 'products': products})

# def detail(request,c_slug=None):
#     id = request.GET.get('id')
#     patient_list = Patient.objects.all().filter(pk=id)
#
#     # c_page = None
#     # patient_list = None
#     # if c_slug != None:
#     #     c_page = get_object_or_404(Patient, slug=c_slug)
#     #     patient_list = Patient.objects.all().filter(branch=c_page, available=True)
#     # else:
#     #     patient_list = Patient.objects.all().filter(available=True)
#
#     return render(request, "hospitaldetails.html",{'hospital_list':hospital_list})

 # def cancel(request):
 #    return redirect('/')


def cancel(request):
    return redirect('/')
def print(request):
    return redirect('/')