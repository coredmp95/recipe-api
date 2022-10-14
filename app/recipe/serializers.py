""""Serializers for Recipes"""

from rest_framework import serializers

from core.models import Recipe, Tag


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Detail serializer for Recipe"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_field = ['id']
