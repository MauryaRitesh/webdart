from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name',max_length=100)
    email = forms.EmailField(max_length=30)
    address = forms.CharField(max_length=200)
    number = forms.IntegerField()
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    code = forms.IntegerField()

class Profile(forms.Form):
	name = forms.CharField(required = True, max_length = 20, help_text = 'Your IG user name.')
    