from django.db import models
from django.contrib.auth.models import User
import hashlib

class Tweet(models.Model):
    text=models.TextField(max_length=2000)
    time=models.DateTimeField(auto_now_add=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.text

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    follows=models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    
    # def gravatar_url(self):
    #     return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

   
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

#The above line states that the User model's object's 'profile' attribute is equal to a Profile object that either gets created or fetched
#This User object can now access the 'follows' attribute of the Profile object as shown below in the second line.
#So what's the logical correlation between superUser.profile and .follows.all()? 
#It is that when you want to access all the 'follows' values, you will ideally do it through a User and hence a User object.

#superUser = User.object.get(id=1)
#superUser.profile.follows.all() # Will return an iterator of UserProfile instances of all users that superUser follows
#superUser.profile.followed_by.all() # Will return an iterator of UserProfile instances of all users that follow superUser