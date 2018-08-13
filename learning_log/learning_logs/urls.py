"""定义learning_log 的URL模式"""

from django.conf.urls import url

from . import views


urlpatterns = [
    #主页
    url(r'^$', views.index, name='index.html'),

    #显示所有主题
    url(r'^topics/$',views.topics,name='topics'),
]
