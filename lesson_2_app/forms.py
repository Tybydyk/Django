from django import forms
import datetime
from . import models

class AuthorForms(forms.Form):
    name = forms.CharField(label='req*', max_length=70, widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                                   'placeholder': 'author name'}))
    surname = forms.CharField(label='req*', max_length=70, widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                                   'placeholder': 'author surname'}))
    email = forms.EmailField(label='req*',
                             widget=forms.TextInput(attrs={'class': 'input_text long_input'}))
    biography = forms.CharField(initial='Biography', label='',
                                widget=forms.TextInput(attrs={'class': 'input_text long_input'}))
    birthday = forms.DateField(initial=datetime.date.today(), label='',
                               widget=forms.DateInput(attrs={'class': 'input_text long_input', 'type': 'date'}))

class NewArticleForm(forms.Form):
    # authors = [(obj.id, obj.full_name()) for obj in models.Author.objects.all()]
    title = forms.CharField()
    # author = forms.ChoiceField(choices=authors)
    author = forms.ModelChoiceField(queryset=models.Author.objects.all(), empty_label='choice author')
    text = forms.CharField(widget=forms.Textarea())

class ArticleForm(forms.ModelForm):

    class Meta:
        model = models.Article
        fields = ['title', 'author', 'content', 'published']
        labels = {'title': '', 'author': '', 'content': '', 'published': ''}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_text long_input', 'placeholder': 'article title'}),
            'author_id': forms.Select(attrs={'class': 'input_text long_input'}),
            'content': forms.Textarea(
                attrs={'class': 'input_text long_input', 'cols': 100, 'rows': 10,'placeholder': 'article content'}),
            'published': forms.DateInput(attrs={'class': 'input_text long_input', 'type': 'date'})
        }
