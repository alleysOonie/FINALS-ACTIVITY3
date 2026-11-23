from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Profile, Post

def profile_page(request):
    profile, _ = Profile.objects.get_or_create(pk=1)
    if not profile.profile_picture:
        # Initial profile image is supplied in media/profile_pictures/profile.jpg.
        profile.profile_picture = "profile_pictures/profile.jpg"
        profile.save(update_fields=["profile_picture"])
    if not profile.posts.exists():
        Post.objects.create(profile=profile, content="free palestine until palestine free 🍉")
        Post.objects.create(
            profile=profile,
            content="Ang bayang dapat pinagsisilbihan ay siya pang ninanakawan; sa kamay ng mga ganid sa kapangyarihan, ang kaban ng bayan ay nagiging kanilang sariling kayamanan."
        )
    return render(request, "profile/profile.html", {"profile": profile, "posts": profile.posts.all()})

@require_POST
def upload_profile_picture(request):
    profile, _ = Profile.objects.get_or_create(pk=1)
    uploaded = request.FILES.get("profile_picture")
    if uploaded:
        if not uploaded.content_type.startswith("image/"):
            messages.error(request, "Please choose an image file.")
        elif uploaded.size > 5 * 1024 * 1024:
            messages.error(request, "Image must be 5 MB or smaller.")
        else:
            profile.profile_picture = uploaded
            profile.save()
            messages.success(request, "Profile picture updated!")
    else:
        messages.error(request, "Choose an image before uploading.")
    return redirect("profile")
