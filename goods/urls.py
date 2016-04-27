from django.conf.urls import url
from goods.views import GoodsListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', GoodsListView.as_view(), name="goods_index"),
    url(r'^(?P<pk>\d+)/detail/$', GoodDetailView.as_view(), name="goods_detail"),
    url(r'^(?P<pk>\d+)/add/$', GoodCreate.as_view(), name="goods_add"),
    url(r'^(?P<pk>\d+)/edit/$', GoodUpdate.as_view(), name="goods_edit"),
    url(r'^(?P<pk>\d+)/delete/$', GoodDelete.as_view(), name="goods_delete"),
]
