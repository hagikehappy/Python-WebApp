from django.shortcuts import render

from .models import Topic


# Create your views here.
def index(request):
    """学习笔记主页"""
    # 这里第二项是网页的本地文件位置，这里的根目录是templates而非django的根目录
    # 因此该目录表明该文件在项目中的相对位置是learning_logs/template/learning_logs/index.html
    return render(request, 'learning_logs/index.html')


def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    # context是一个字典，用于在模板中传递数据给网页html文件
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    # 接收urls传入的捕获
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   # 根据日期降序排列
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

