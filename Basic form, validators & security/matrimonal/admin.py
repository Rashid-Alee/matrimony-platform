from django.contrib import admin
from .models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "gender", "occupation", "email"]
    list_display_links = ["name", "email"]
    list_filter = ["occupation", "is_married"]
    search_fields = ["name"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Religion)
admin.site.register(Sects)
admin.site.register(Caste)


class HobbyAdmin(admin.ModelAdmin):
    list_display = ["name", "get_profiles"]

    def get_profiles(self, obj):
        hobby_followers = ", ".join([profile.name for profile in obj.profiles.all()])
        return hobby_followers

    get_profiles.short_description = "profiles"


admin.site.register(Hobby, HobbyAdmin)
admin.site.register(FatherProfile)
