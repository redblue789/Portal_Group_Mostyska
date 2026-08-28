from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materials/', include('materials.urls')), # Переконайтеся, що цей рядок є!
]

# Важливо для відображення завантажених файлів та картинок під час розробки:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)