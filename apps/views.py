from django.template import Context, loader
from hjemmeside.apps.models import Application
from django.shortcuts import render_to_response
from django.views.generic import list_detail

def list(request, page = 0):
	return list_detail.object_list(
            request, 
            queryset = Application.objects.all(), 
            paginate_by = 5, 
            page = page)

def get_app(request, app_id):
	return list_detail.object_detail(
            request, 
            queryset = Application.objects.all(), 
            object_id = app_id)

