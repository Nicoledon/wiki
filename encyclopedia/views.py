from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect
class NewTaskForm(forms.Form):
      task = forms.CharField(
          widget=forms.TextInput(attrs={
             'class': 'search',
             'placeholder':'Search Encyclopedia'
            })
      )
tasks = util.list_entries()
def index(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            if task in tasks:
                return HttpResponseRedirect(reverse("page", args=[task]))
            else :
                return render(request , "encyclopedia/index.html", {
                       "form":form
                })
    else:
        return render(request, "encyclopedia/index.html", {
           "entries": util.list_entries(),
           "form" : NewTaskForm()
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
def modify(request):

    return render(request, "encyclopedia/modify.html")