from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm


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
    # 接收urls传入的捕获，从数据库中查询
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   # 根据日期降序排列
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 此时请求类型为GET，未提交数据
        form = TopicForm()
    else:
        # POST提交的数据：对数据进行处理
        form = TopicForm(data=request.POST)
        # 检查输入数据是否有效
        if form.is_valid():
            form.save()
            # 重定向
            return redirect('learning_logs:topics')

    # 显示空表单或指出表单数据无效
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """在特定主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)     # 保存到数据库中
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # 显示空表单或指出表单数据无效
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
