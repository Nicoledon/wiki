from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect
import random
import markdown2
class NewTaskForm(forms.Form):
      task = forms.CharField(
          widget=forms.TextInput(attrs={
             'class': 'search',
             'placeholder':'Search Encyclopedia'
            })
      )
class NewModifyTaskForm(forms.Form):
      headline =  forms.CharField(label= "headline" , widget=forms.Textarea(attrs={
          'class': 'form-control',
          'style' : 'width:300px; height:40px'
      }))
      content =  forms.CharField(label= "content", widget=forms.Textarea(attrs={
           'class':'form-control',
           'style':'width:300px;height;200px',
      }))


class NewEditTaskForm(forms.Form):
      content = forms.CharField(label = "content", widget=forms.Textarea(attrs={
           'class':'form-control',
           'style':'width:300px;height;200px',
           'row':3
      }
      ))  
      def __init__(self, *args, content_placeholder=None, **kwargs):
        super().__init__(*args, **kwargs)
        if content_placeholder:
            self.fields['content'].widget.attrs['placeholder'] = content_placeholder
tasks = util.list_entries() 
def option(str):
    container = []
    for task in tasks:
        if str in task:
            container.append(task)
    return container
def index(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            if task in tasks:
                return HttpResponseRedirect(reverse("page", args=[task]))
            else :
                container = option(task)
                return render(request ,"encyclopedia/option.html" , {
                    "container":container 
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
       html = markdown2.markdown(util.get_entry(headline))
   return render(request, "encyclopedia/page.html", {
        "headline":headline,
         "content":html,
         "exist" : exist 
    })
def modify(request):
    if request.method == "POST":
        form = NewModifyTaskForm(request.POST)
        if form.is_valid():
            headline = form.cleaned_data["headline"]
            content = form.cleaned_data["content"]
            util.save_entry(headline,content)
            return HttpResponseRedirect(reverse("index"))      
        else :
            return render(request, "encyclopedia/modify.html", {
                   "newform": form
        })
    else:
        return render(request, "encyclopedia/modify.html", {
            "newform": NewModifyTaskForm()
    })
def edit(request, elem):
    if request.method == "POST":
        form = NewEditTaskForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(elem,content)
            return HttpResponseRedirect(reverse("index"))      
        else :
            return render(request, "encyclopedia/edit.html", {
                   "elem":elem, 
                   "contentedit": form
        })
    else :
        return render(request, "encyclopedia/edit.html", {
               "elem":elem,
               "contentedit":NewEditTaskForm(content_placeholder=util.get_entry(elem))
        })
def randoms(request):
    container = util.list_entries()
    item = random.choice(container)
    return HttpResponseRedirect(reverse("page",args=[item]))