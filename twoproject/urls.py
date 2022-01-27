
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.posts),
    path('<int:dic>',views.numbers),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.posts, name='post_list'),
    path('post/<int:pk>/', views.post, name="post_detail"),
    path('main/',views.main),
    path('blog/',views.blog),
    path('forme', views.forMe),
]
