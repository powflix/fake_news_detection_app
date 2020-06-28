from django import forms


class url_form(forms.Form):
    news_url = forms.URLField(label='News url', max_length=500)
