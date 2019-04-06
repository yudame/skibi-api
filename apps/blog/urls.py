from django.conf.urls import url

from apps.blog.views.article import ArticleView
from apps.blog.views.topic import TopicView
from apps.blog.views.blog import BlogView

app_name = 'blog'

urlpatterns = [

    url(r'^(?P<blog_slug>[-\w\.]+)$',
        BlogView.as_view(), name='blog'),

    url(r'^(?P<blog_slug>[-\w\.]+)/topic/(?P<topic_slug>[-\w\.]+)$',
        TopicView.as_view(), name='topic'),

    url(r'^(?P<blog_slug>[-\w\.]+)/article/(?P<article_slug>[-\w\.]+)$',
        ArticleView.as_view(), name='article'),
]