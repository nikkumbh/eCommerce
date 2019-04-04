from __future__  import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
# Create your models here.

class profiles(models.Model):
	name = models.CharField(max_length = 120)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete = models.PROTECT)
	description = models.TextField(default = 'Description here!')
	location = models.CharField(max_length = 200,null = True,blank = True)
	job = models.CharField(max_length = 250)

	def __unicode__(self):
		return self.name

class userStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.PROTECT)
	stripe_id = models.CharField(max_length=254,null=True,blank = True)

	def __unicode__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username	

def profileCallback(sender,request,user,**kwargs):
	userProfile,is_created = profiles.objects.get_or_create(user = user)
	if is_created:
		userProfile.name = user.username
		userProfile.save()			

user_signed_up.connect(profileCallback)	