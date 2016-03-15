# -*- coding: utf-8 -*-
from django.views.generic import FormView
from recipe_search.forms import SearchForm
from recipe_search.models import Recipe
from django.shortcuts import render_to_response
from django.template.context import RequestContext


class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def form_valid(self, form):
        cd = form.cleaned_data

        recipes = Recipe.objects.prefetch_related('variations__ingredient').filter(title__icontains=cd['title'])
        context = self.get_context_data()
        context['recipes'] = recipes

        return render_to_response(self.template_name, context, context_instance=RequestContext(self.request))
