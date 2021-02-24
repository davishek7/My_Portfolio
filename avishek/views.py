import os
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Post

def sendemail(request):

	posts=Post.objects.all()

	if request.method=="POST":
		name=request.POST['name']
		subject=request.POST['subject']
		email=request.POST['email']
		message=request.POST['message']
		
		send_mail(
			f'{subject} from {name}({email})',
			message,
			email,
			[os.environ.get('RECEIVER_EMAIL')]
		)
		messages.success(request,f'Thank you, {name} for contacting me,I will be back to you shortly.')
		return redirect('email')	
	
	return render(request,'avishek/index.html',{'posts':posts})


