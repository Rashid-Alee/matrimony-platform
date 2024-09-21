from django.shortcuts import render
from .models import Profile

# Create your views here.


def ProfileListView(request):
    profiles = Profile.objects.all()
    return render(request, "matrimonal/Profile_List.html", {"profiles": profiles})


def ProfileDetailView(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, "matrimonal/Profile_Detail.html", {"profile": profile})
