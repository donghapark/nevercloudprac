from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import mimetypes

from posts.views import index, url_view, url_paramater_view , function_view ,class_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/',url_view),
    path('url/<str:username>/',url_paramater_view),
    path('fbv/',function_view),
    path('cbv/',class_view.as_view()),

    path('', index, name='index'),

    path('posts/', include('posts.urls',namespace='posts')),

    path('__debug__/', include('debug_toolbar.urls')),

    

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


mimetypes.add_type("application/javascript", ".js", True)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]