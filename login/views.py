from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth import logout


def index(request):

	template = loader.get_template('index.html')
	ctx = {}
	return HttpResponse(template.render(ctx,request))

def logOut(request):
	logout(request)
	return redirect('/')
	
