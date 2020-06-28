from django import forms


class news_form(forms.Form):
    heading = forms.CharField(label='heading')
    content = forms.CharField(label='content')
