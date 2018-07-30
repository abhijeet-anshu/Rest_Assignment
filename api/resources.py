# api/resources.py
from tastypie.resources import ModelResource
from api.models import Data
from django.conf.urls import url
from django.views.defaults import page_not_found
class APIResource(ModelResource):
    class Meta:
        queryset = Data.objects.all()
        resource_name = 'data'
        fields = ['key', 'value']
        allowed_methods = ['get']
        detail_uri_name = 'value' 
    def prepend_urls(self):
    	return [url(r'^(?P<value>.*?)/$', self.wrap_view('dispatch_detail'), 
    				name="api_dispatch_detail"),]
    def dehydrate(self, bundle):
    	del bundle.data['resource_uri']
    	return bundle
