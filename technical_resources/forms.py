# created by Chirath R <chirath.02@gmail.com>
from django import forms

from technical_resources.models import Category, Files, Links


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category name',  help_text='Enter category name, example: Python, C, OS...',
                           widget=forms.TextInput(attrs={'placeholder': 'DBMS, Ruby, NodeJS....'}))

    description = forms.CharField(label='Description', help_text='Describe about the category',
                                  widget=forms.Textarea(attrs={'placeholder': 'Info about this category'}))

    image = forms.ImageField(label='Image', help_text='Add an image')

    class Meta:
        model = Category
        fields = ['name', 'image', 'description']


class LinksForm(forms.ModelForm):
    name = forms.CharField(label='Link name', help_text='Enter a name to show for the link',
                           widget={'placeholder': 'Link name'})

    link = forms.URLField(label='Url', help_text='Enter the url', widget={'placeholder': 'https://www.....'})

    class Meta:
        model = Links
        fields = ['name', 'link']


class FilesForm(forms.ModelForm):
    name = forms.CharField(label='Link name', help_text='Enter a name to show for the link',
                           widget={'placeholder': 'Link name'})

    file = forms.FileField(label='Select file', help_text='Select a file')

    class Meta:
        model = Files
        fields = ['name', 'file']
