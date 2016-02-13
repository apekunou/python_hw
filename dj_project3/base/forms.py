from django import forms




class PlayerEmailFilter(forms.Form):
    email = forms.EmailField(label='Email')

class PlayerChangeExp(forms.Form):
    name = forms.CharField(label='Name', max_length=45)
    xp = forms.IntegerField(label='Expa')