from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile = models.ImageField(upload_to = 'profiles/')
    username = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 500)
    Flashes = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts = models.CharField(max_length = 50)


    # Methods
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    

    @classmethod
    def get_profile(cls, profile_id):
        profile = Profile.objects.filter(name__username__icontains=profile_id)
        return profile

class Flashes(models.Model):
    User = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    @classmethod
    def search_by_subject(cls,search_term):
        flashes = cls.objects.filter(subject__icontains=search_term)
        return flashes


    # Methods
    def save_flashes(self):
        self.save()

    def delete_flashes(self):
        self.delete()

    def update_flashes():
        self.update()











