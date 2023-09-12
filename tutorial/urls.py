"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groupd', views.GroupViewSet)
# In Python, %r and %s are used as string formatting operators to
# insert values into a string. The %s operator is used for representing 
# strings, wheres %r is used to represent a string as it would appear in
# its raw form, including quotes and special characters.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Because we're using viewsets instead of views, we can automatically
    # generate the URL conf for our API, by simply registering the viewsets
    # with a router class.
    path('', include(router.urls)),
    # Finally, we're including default login and logout views for use with
    # the browsable API. That's optional, but useful if your API requires
    # authentication and you want to use the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
