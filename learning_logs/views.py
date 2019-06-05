from django.shortcuts import render
from .models import Topic
from django.http import HttpResponse

"""
视图函数用于提供URL要显示的内容，
可以是纯文本      例如return HttpResponse('HELLO WORLD')
也可以是html页面  例如return render(request, 'logs/index.html') 
                          render(谁发起的请求，收到请求后返回的页面，[页面所需的数据])
"""

# Create your views here.
def index(request):
    """主页"""
    return render(request, 'logs/index.html')
    # return HttpResponse('HELLO WORLD')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'logs/topics.html', context)


def topic(request, topic_id):
    """显示单个主题的所有条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'logs/topic.html', context)
