from app.models import *
from django import forms
from app.forms import *


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForms(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name','url']
        #exclude=['name']
        #labels={'topic_name':'Topic','name':'Name'}
        #widgets={'name':forms.PasswordInput}




class AccessRecordForms(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
    