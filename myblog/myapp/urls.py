from django.conf.urls import url
from myapp.views import list_view, detail_view, post_new, APIPostList

urlpatterns = [
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),  # Add this line
    url(r'^apiposts/', APIPostList.as_view()),
    url(r'^$', list_view, name="blog_index"),
]
