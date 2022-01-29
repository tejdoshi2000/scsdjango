from django.shortcuts import render

from .models import enquiry

# Create your views here.

def index(request):
    return render(request , "indexV5.html")

def contact(request):
    if request.method == "POST":
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        Email = request.POST.get("Email")
        PhoneNumber = request.POST.get("PhoneNumber")
        Address = request.POST.get("Address")
        Organization = request.POST.get("Organization")
        Requirements = request.POST.get("Requirements")

        inquiry = enquiry(FirstName = FirstName ,LastName = LastName, Email = Email , PhoneNumber = PhoneNumber , Address = Address , Organization = Organization , Requirements = Requirements)
        inquiry.save()

        return render(request , "contactV5.html" , {"Suc" : True} )

    return render(request , "contactV5.html")
