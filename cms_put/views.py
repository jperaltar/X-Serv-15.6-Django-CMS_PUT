from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden

# Create your views here.

def main(request, resource):
    if request.method == "GET":
        try:
            page_entry = Pages.objects.get(name=resource)
            return HttpResponse(page_entry.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound(
                'Page not found: /%s.' % resource)
    elif request.method == "PUT":
        new_entry = Page(name=resource, page=request.body)
        new_entry.save()
        return HttpResponse("Succesful PUT operation: " 
                            + request.body)
    else:
        return HttpResponseForbidden("Operation not available")
