from django.conf.urls import url

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name="blog_index"),
    url(r'^(?P<pk>\d+)/detail/$', BlogDetailView.as_view(), name="blog_detail"),
    url(r'^(?P<pk>\d+)/add/$', BlogCreate.as_view(), name="blog_add"),
    url(r'^(?P<pk>\d+)/edit/$', BlogUpdate.as_view(), name="blog_edit"),
    url(r'^(?P<pk>\d+)/delete/$', BlogDelete.as_view(), name="blog_delete"),
]
