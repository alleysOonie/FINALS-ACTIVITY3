from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profile.views import profile_page, upload_profile_picture

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", profile_page, name="profile"),
    path("upload-profile-picture/", upload_profile_picture, name="upload_profile_picture"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
