from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core import serializers
from django.core.urlresolvers import reverse

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

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(LocationCreateView, self).form_valid(form)

  def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class LocationUpdateView(LoginRequiredMixin, UpdateView):
  model = Location
  template_name = 'app/location_update_form.html'
  fields = ['lat', 'lng', 'title', 'note']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(LocationUpdateView, self).form_valid(form)

  def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

class LocationDeleteView(LoginRequiredMixin, DeleteView):
  model = Location
  fields = ['lat', 'lng', 'title', 'note']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(LocationUpdateView, self).form_valid(form)

  def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})
