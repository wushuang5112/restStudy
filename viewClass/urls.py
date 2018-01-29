from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from viewClass import views

urlpatterns = [
    url(r'^snippets3/$', views.SnippetList.as_view()),
    # url(r'^snippets_detail3/$', views.SnippetDetail.as_view()),
    url(r'^snippets3/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

