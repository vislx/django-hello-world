from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail_question'),
    url(r'^(?P<pk>[0-9]+)/result/$', views.ResultView.as_view(), name='vote_result'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]