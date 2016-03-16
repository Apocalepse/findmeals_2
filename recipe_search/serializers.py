from rest_framework import serializers
from .models import Recipe, Variation


class RecipeSerializer(serializers.ModelSerializer):
    variations = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ('title', 'variations',)
