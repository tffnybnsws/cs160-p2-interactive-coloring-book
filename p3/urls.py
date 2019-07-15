from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coloring/', include('coloring.urls')),
    #path('coloring/palette', include('coloring.urls'))
]
