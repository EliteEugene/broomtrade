from django.conf.urls import url
from imagepool.views import get_list, upload_file, delete_file

urlpatterns = [
    url(r'^$', get_list, name="imagepool_index"),
    url(r'^upload/$', upload_file, name="imagepool_upload"),
    url(r'^(?P<pk>\d+)/delete/$', delete_file, name="imagepool_delete"),
]
