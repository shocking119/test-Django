from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm,EntryForm

def index(request):
    '''index'''
    app_name = 'learnings'
    return render(request,'learnings/index.html')
def topics(request):
    #显示所有主题
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learnings/topics.html',context)
def topic(request,topic_id):
    #显示单个主题及其条目
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learnings/topic.html',context)
def new_topic(request):
    #添加新主题
    if request.method != 'POST':     #未提交数据则创建新表单
        form = TopicForm()
    else:                            #提交数据则对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learnings:topics'))

    context = {'form':form}
    return render(request,'learnings/new_topic.html',context)

def new_entry(request,topic_id):
    #特定主题添加新条目
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':     #未提交数据则创建新表单
        form = EntryForm()
    else:                            #提交数据则对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learnings:topics',args=[topic_id]))

    context = {'topic':topic,'form':form}
    return render(request,'learnings/new_entry.html',context)

def edit_entry(request,entry_id):
    '''编辑既有条目'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        #初次请求使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        #对post提交的数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learnings:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learnings/edit_entry.html',context)
