# -*- coding: utf-8 -*-
from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(label=u'Название')

