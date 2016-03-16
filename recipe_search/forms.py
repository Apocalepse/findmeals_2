# -*- coding: utf-8 -*-
from django import forms
from djng.forms import NgModelFormMixin
from djng.styling.bootstrap3.forms import Bootstrap3Form


class SearchForm(NgModelFormMixin, Bootstrap3Form):
    scope_prefix = 'search_data'
    form_name = 'search_form'

    title = forms.CharField(label=u'Название')
