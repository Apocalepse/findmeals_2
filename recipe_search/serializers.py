from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    variations = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ('title', 'variations',)
