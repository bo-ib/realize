from django.forms import ModelForm
from . models import Article,Comment
from django import forms


class BlogForm(ModelForm):
    class Meta:
      model = Article
      fields = "__all__"



class CommentForm(ModelForm):
 
  class Meta:
    model =Comment
    fields = ('name', 'Email','body')
    widgets ={
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'Email':forms.EmailInput(attrs={'class':'form-control'}),
      'body':forms.Textarea(attrs={'class':'form-control','cols': 3, 'rows': 3}),
    }
    



    