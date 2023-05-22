from django import forms
from .models import Message
class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "contact__input"}))
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "contact__input"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "contact__input"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':"0",'rows':"7", 'class': "contact__input"}))
    class Meta:
        model = Message
        fields = ('name', 'title', 'email', 'message', )