from django.shortcuts import render, redirect
from django.http import HttpResponse
from firstapp.models import Topic
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['top_name']


class TopicCreate(CreateView):
    model = Topic
    fields = ['id', 'top_name']
    success_url = reverse_lazy('firstapp:book_list')

def create_topic(request, template_name='topic/build_topic.html'):
    return redirect('http://google.com')

def build_topic(request, template_name='topic/build_topic.html'):
    form = TopicForm(None)
    return render(request, template_name, {'form': form})
