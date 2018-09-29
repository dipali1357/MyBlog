from django.shortcuts import render
from rango.models import Category,Page
from django.http import HttpResponse

"""construct a dictionary to pass to a template as its context 
the key is boldmessage 
return a rendered response to send to client as below in index view"""

def index(request):
    category_list=Category.objects.order_by('-likes')[:5]
    context_dict={'categories' : category_list}
    return render(request,'rango/index.html',context=context_dict)

def show_category(request,category_name_url):
	category_name_url=''

def about(request):
	context_dict2={'msg' : "This tutorial has been put together by django",}
	return render(request,'rango/about.html',context=context_dict2)

def trial(request):
	context_dict1={'new_msg': "THIS IS MY SPECIAL MESSAGE TO YOU",}
	return render(request, 'rango/trial.html',context=context_dict1)