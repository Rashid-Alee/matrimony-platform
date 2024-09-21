from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm, ProfileForm
from django.contrib import messages

# Create your views here.


def ProfileListView(request):
    profiles = Profile.objects.all()
    return render(request, "matrimonal/Profile_List.html", {"profiles": profiles})


def ProfileDetailView(request, profile_id):
    profiles = Profile.objects.get(id=profile_id)
    return render(request, "matrimonal/Profile_Detail.html", {"profile": profiles})


def ProfileDeleteView(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    profiles = Profile.objects.all()

    return render(request, "matrimonal/Profile_List.html", {"profiles": profiles})


def ContactView(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(request, "Your form has been successfully sent!")
            return render(request, "matrimonal/contact.html", {"form": form})

    else:
        form = ContactForm()

    return render(request, "matrimonal/contact.html", {"form": form})


def NewProfileView(request):

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("matrimonal:Profile_List")

    else:
        form = ProfileForm()

    return render(request, "matrimonal/new_Profile.html", {"form": form})
