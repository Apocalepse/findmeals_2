from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from recipe_search.views import SearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SearchView.as_view()),
]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
