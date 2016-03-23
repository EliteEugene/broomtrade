from django.conf.urls import url

from news.views import NewsListView, NewDetailView, NewCreate, NewUpdate, NewDelete


urlpatterns = [
    url(r'^$', NewsListView.as_view(), name="news_index"),
    url(r'^(?P<pk>\d+)/$', NewDetailView.as_view(), name="news_detail"),
    url(r'^add/$', NewCreate.as_view(), name="news_add"),
    url(r'^(?P<pk>\d+)/edit/$', NewUpdate.as_view(), name="news_edit"),
    url(r'^(?P<pk>\d+)/delete/$', NewDelete.as_view(), name="news_delete"),
]
