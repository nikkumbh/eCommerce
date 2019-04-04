from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def contact(request):
	form = ContactForm(request.POST or None)
	title = 'Contact'
	context ={'title':title,'form':form,}
	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Message from MySite'
		message = '%s %s' %(comment,name)
		emailFrom =  form.cleaned_data['email']
		emailTo =  [settings.EMAIL_HOST_USER]
		send_mail(subject,message,emailFrom,emailTo,fail_silently=False)
		title = 'Thanks!'
		confirm_message = "Thanks for the message. We will get right back to you."
		context = {'title':title,'confirm_message':confirm_message,}

	template = 'contact/contact.html'
	return render(request,template,context)