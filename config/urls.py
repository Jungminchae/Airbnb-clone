from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path("reservations/", include("reservations.urls", namespace="reservations")),
    path("reviews/", include("reservations.urls", namespace="resviews")),
    path("lists/", include("lists.urls", namespace="lists")),
    path("conversations/", include("conversations.urls", namespace="conversations")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
