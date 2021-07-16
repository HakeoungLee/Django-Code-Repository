# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

# class PostForm(forms.Form):  # django의 폼을 상속
#     title = forms.CharField(label='제목', max_length=200)
#     content = forms.CharField(label="내용", widget=forms.Textarea)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('Title'),
            'content': _('Content'),
        }
        help_texts = {
            'title': _('Type Title'),
            'content': _('Type Content'),
        }
        error_messages = {
            'name': {
                'max_length': _("Please shorten your title."),
            },
        }
