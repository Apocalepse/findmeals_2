from django.conf.urls import url
from django.contrib import admin
from recipe_search.views import SearchView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SearchView.as_view()),
]
