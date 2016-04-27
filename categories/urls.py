from django.conf.urls import url
from categories.views import CategoriesEdit

urlpatterns = [
    url(r'^$', CategoriesEdit.as_view(), name="categories_edit"),
]
