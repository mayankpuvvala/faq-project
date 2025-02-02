from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


def home(request):
    return HttpResponse(
        "Welcome to the FAQ API! Use /api/faqs/ to access the FAQ list.")


urlpatterns = [
    path('', home),  # Root URL
    path('api/', include('faq.urls')),  # API URLs
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
