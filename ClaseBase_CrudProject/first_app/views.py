from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView
from first_app import models
from first_app import forms
from django.urls import reverse_lazy
# Create your views here.

class index(ListView):
    context_object_name="Musician_list"
    model=models.Musician
    template_name="first_app/index.html"

class addmusician(CreateView):
    model=models.Musician
    fields="__all__"
    template_name="first_app/addmusician.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["title"]="Add Musician"
        context["title1"]="Add musician"
        return context
class addalbum(CreateView):
    model=models.Album
    fields="__all__"
    template_name="first_app/addalbum.html"

class Musiciandetails(DetailView):
    context_object_name="musician_list"

    model=models.Musician
    template_name="first_app/musiciandetails.html"
class updatemusician(UpdateView):
    model=models.Musician
    fields="__all__"
    template_name="first_app/updatemusician.html"
class updatealbum(UpdateView):
    model=models.Album
    fields="__all__"
    template_name="first_app/updatealbum.html"
class musiciandelete(DeleteView):
    context_object_name="musician"
    model=models.Musician
    success_url=reverse_lazy('first_app:index')
    template_name="first_app/musiciandelete.html"
# class albumdelete(DeleteView):
#     model=models.Album
#     context_object_name='album'
#     success_url=reverse_lazy('first_app:index')
#     template_name="albumdelete.html"
