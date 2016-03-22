# -*- coding: utf-8 -*-
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    gender = forms.ChoiceField(choices = [('1','1'), ('2','2'),('3','3'), ], required = True, widget=forms.RadioSelect)

