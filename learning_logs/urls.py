"""定义learning_logs的URL模式"""
from django.urls import path

from . import views


app_name = 'learning_logs'
# 包含可在应用程序中使用的网页
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面，第一个参数是django的路由模式匹配
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
