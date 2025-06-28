from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request , headline):
   entries = util.list_entries()
   exist = False
   if headline in entries:
       exist = True
   return render(request, "encyclopedia/page.html", {
        "headline":headline,
         "content":util.get_entry(headline),
         "exist" : exist 
    })
