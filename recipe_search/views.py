# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models.query import Prefetch
from django.http import HttpResponseBadRequest

from rest_framework.response import Response

from recipe_search.forms import SearchForm
from recipe_search.models import Recipe, Variation
from recipe_search.serializers import RecipeSerializer
from rest_framework.views import APIView


class SearchView(APIView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        return render_to_response(self.template_name,  {'form': form}, context_instance=RequestContext(self.request))

    def post(self, request, *args, **kwargs):

        if not request.is_ajax():
            return HttpResponseBadRequest('Expected an XMLHttpRequest')

        in_data = request.data

        bound_search_form = SearchForm(data={'title': in_data.get('title')})

        if bound_search_form.is_valid():

            cd = bound_search_form.cleaned_data

            recipes = Recipe.objects.prefetch_related(
                Prefetch('variations', queryset=Variation.objects.select_related('ingredient'))
            ).filter(title__icontains=cd['title'])

            serializer = RecipeSerializer(recipes, many=True)

            return Response(serializer.data)
        else:
            print request.body
