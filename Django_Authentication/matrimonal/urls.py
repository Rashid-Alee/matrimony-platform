from django.contrib import admin
from django.urls import path

from . import views

app_name = "matrimonal"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.ProfileListView, name="Profile_List"),
    path("<int:profile_id>", views.ProfileDetailView, name="Profile_Detail"),
    path("<int:profile_id>/delete", views.ProfileDeleteView, name="Profile_delete"),
    path("contact", views.ContactView, name="contact"),
    path("new_Profile", views.NewProfileView, name="new_Profile"),
]
