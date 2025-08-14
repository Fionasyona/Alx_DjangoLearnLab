from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Temporary home view (replace with your real app later)
def home(request):
    return HttpResponse("<h1>Welcome to Django Blog</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL will now work
     path("", include(("blog.urls", "blog"), namespace="blog")),  # home -> posts list
    # auth urls if you use Django auth views:

    # Blog routes (only if you have a blog app)
    # path('', include('blog.urls')),  # Uncomment when ready

    # Users routes (commented out until 'users' app is created)
    # path('login/', include('users.urls')),
    # path('register/', include('users.urls')),
    # path('profile/', include('users.urls')),
]

# Serve static & media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
