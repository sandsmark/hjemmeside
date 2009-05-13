from django.template import Context, loader
from hjemmeside.blog.models import Entry
from django.shortcuts import render_to_response
from django.views.generic import list_detail

def list(request, page = 0):
	return list_detail.object_list(
            request, 
            queryset = Entry.objects.all(), 
            paginate_by = 5, 
            page = page)

def get_entry(request, entry_id):
	return list_detail.object_detail(
            request, 
            queryset = Entry.objects.all(), 
            object_id = entry_id)

