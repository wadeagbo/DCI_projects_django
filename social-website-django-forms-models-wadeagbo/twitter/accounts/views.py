from django.views.generic import TemplateView, View
from django.shortcuts import render
from .models import UserProfile

class ProfileView(TemplateView):
    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        followers = user_profile.followers.all()
        user_profiles = UserProfile.objects.exclude(user=user)

        return render(
            request,
            "accounts/profile.html",
            {"followers": followers, "user_profiles": user_profiles},
        )

    def post(self, request):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)        
        
        # do not touch code in lines above
        # TODO: Add logic to update the followers (Use the FollowForm provided in forms.py)

        # End of task (do not touch code below)
        followers = user_profile.followers.all()
        user_profiles = UserProfile.objects.exclude(user=user)

        return render(
            request,
            "accounts/profile.html",
            {"followers": followers, "user_profiles": user_profiles},
        )