from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.ArticleList.as_view(), name="article_list"),
)
