"""Url mapping for the recipe API"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipe', views.RecipeViewSet)

app_name = 'recipe'

url_patterns = [
    path('', include(router.urls)),
]
