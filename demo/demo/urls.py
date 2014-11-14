from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include("articles.urls"))

    # url(r'^admin/', include(admin.site.urls)),
)
