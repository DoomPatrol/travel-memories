from __future__ import absolute_import, unicode_literals
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(r'^$', views.AllLocationsView.as_view(), name='all-locations'),
    url(r'^add-location/', views.LocationCreateView.as_view(), name='add-location'),
    url(r'^edit-location/(?P<pk>[\w-]+)$', views.LocationUpdateView.as_view(), name='edit-location'),
    url(r'^delete-location/(?P<pk>[\w-]+)$', views.LocationDeleteView.as_view(), name='delete-location'),

    ]
