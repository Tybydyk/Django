from django import forms
import datetime

class GameForm(forms.Form):
    choice = forms.ChoiceField(choices=[('1', 'heads & tails'), ('2', 'Dice'), ('3', "Rand")])
    count = forms.IntegerField(min_value=0, max_value=64, widget=forms.NumberInput(attrs={'class': 'form-control'}))

# class AuthorForms(forms.Form):
#     name = forms.CharField(label='N', max_length=70, widget=forms.TextInput(attrs={'class': 'input_text long_input',
#                                                                                    'placeholder': 'author name'}))
#     surname = forms.CharField(label='N', max_length=70, widget=forms.TextInput(attrs={'class': 'input_text long_input',
#                                                                                    'placeholder': 'author surname'}))
#     email = forms.EmailField(initial='E-mail', label='',
#                              widget=forms.TextInput(attrs={'class': 'input_text long_input'}))
#     bio = forms.CharField(initial='E-Biography', label='',
#                           widget=forms.TextInput(attrs={'class': 'input_text long_input'}))
#     birthday = forms.DateField(initial=datetime.date.today(), label='',
#                                widget=forms.DateInput(attrs={'class': 'input_text long_input', 'type': 'date'}))
