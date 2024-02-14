
#imports
from django.db.models.signals import post_save #the type of the signal that we want to recieve
from django.contrib.auth.models import User #the user modulle which we will use to create the profile
from django.dispatch import receiver #the receiver which will recieve the save signal
from .models import Profile #the profile module we want to fill and later display


@receiver(post_save,sender=User) #this will check if the user register and click on save , it will call the next function 
def build_profile(sender,instance,created,**kwargs):

    if created: #if the user is created
        Profile.objects.create(user=instance) #crete a profile for the registered user


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs) : #saving the profile
    instance.profile.save()      