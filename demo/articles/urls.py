from django.conf.urls import include, url

from .views import ArticleList

urlpatterns = [
    url(r'^$', ArticleList.as_view(), name="article_list"),
]
