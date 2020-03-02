# -*- coding: utf-8 -*-
from django import forms
class userForm(forms.Form):
    picture = forms.ImageField()