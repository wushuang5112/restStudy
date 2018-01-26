from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from requestResponse import views

urlpatterns = [
    url(r'^snippets2/$', views.snippet_list),
    url(r'^snippets2/(?P<pk>[0-9]+)$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

