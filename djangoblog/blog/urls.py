from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',

    # homepage view
    url(r'^$', 'homepage_view', name='homepage_view'),

    # single post view
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w-]+)$', 
        'post_view', name='post_view'),

    # about me view
    url(r'^about$', 'about_view', name='about_view')
)
