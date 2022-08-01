from django.contrib import admin
from django.urls import path, re_path
from blog.views import home, about
from django.conf.urls import handler404
# from django.views.static import serve 
# from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about-zibar/', about, name="about"),

    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

handler404 = 'blog.views.error_404_view'

# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


