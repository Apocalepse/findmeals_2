# -*- coding: utf-8 -*-
import json
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models.query import Prefetch
from django.http import HttpResponseBadRequest, HttpResponse

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
        # return json.dumps({'ok': 'ok'})

        # if not request.is_ajax():
        #     return HttpResponseBadRequest('Expected an XMLHttpRequest')
        # post_data = json.dumps(request.POST)

        # in_data = json.loads(request.data)
        in_data = request.data

        bound_search_form = SearchForm(data={'title': in_data.get('title')})

        if bound_search_form.is_valid():

            cd = bound_search_form.cleaned_data

            recipes = Recipe.objects.prefetch_related(
                Prefetch('variations', queryset=Variation.objects.select_related('ingredient'))
            ).filter(title__icontains=cd['title'])

            serializer = RecipeSerializer(recipes, many=True)

            # print serializer.data
            #
            return Response(serializer.data)

            # context = self.get_context_data()
            # context['recipes'] = recipes
            # context['form'] = bound_search_form

            # return json.dumps(list(recipes))

            # return render_to_response(self.template_name, context, context_instance=RequestContext(self.request))
        else:
            print request.body


