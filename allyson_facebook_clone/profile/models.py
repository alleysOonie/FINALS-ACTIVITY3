from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=120, default="Allyson Calderon")
    bio = models.CharField(max_length=120, blank=True, default="라미⋆˚࿔")
    intro = models.TextField(blank=True, default="Lives in Lucena City\nStudies at Dalubhasaan ng Lungsod ng Lucena")
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.content[:50]
