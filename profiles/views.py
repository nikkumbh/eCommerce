from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

class IndexView(generic.TemplateView):
	template_name = 'profiles/home.html'

class AboutView(generic.TemplateView):
	template_name = 'profiles/about.html'	

@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profiles/profile.html'
	return render(request,template,context)

