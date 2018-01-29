from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from normalView import views

urlpatterns = [
    url(r'^snippets5/$', views.SnippetList.as_view()),
    # url(r'^snippets_detail5/$', views.SnippetDetail.as_view()),
    url(r'^snippets_detail5/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

print "*" * 80, urlpatterns

