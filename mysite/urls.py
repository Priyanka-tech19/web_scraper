
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.scrape,name="scrape"),
    path('delete/',views.clear,name="clear"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

