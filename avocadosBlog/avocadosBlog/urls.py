from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from posts.api.view import PostApiView
from posts.api.router import router_post

schema_view = get_schema_view(
   openapi.Info(
      title="Blog documentatio API",
      default_version='v2',
      description="Here you will see the documentation of the API to consume on the program",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pablo.cabrera@Alluxi.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HelloWorld.as_view())
    # path('api/posts/', PostApiView.as_view())
    path('api/', include(router_post.urls)),
    path('api/', include('user.api.router')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
