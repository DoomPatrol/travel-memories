from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core import serializers

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from app.models import Location

# Create your views here.
class AllLocationsView(ListView):

  model = Location
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['map_data'] = serializers.serialize('json', self.object_list)
    return context


class LocationCreateView(LoginRequiredMixin, CreateView):
  model = Location
  fields = ['lat', 'lng', 'title', 'note']
  success_url = '/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(LocationCreateView, self).form_valid(form)

