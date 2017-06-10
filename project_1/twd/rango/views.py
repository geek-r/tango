# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	# Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	context_dict={'boldmessage':"I am bold font from the context"}
	return render(request,'rango/index.html',context_dict)

	
