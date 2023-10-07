"""让用户通过表单与网页交互"""
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 小部件
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}




