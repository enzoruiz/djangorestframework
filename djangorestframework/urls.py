"""djangorestframework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/token', obtain_jwt_token),
    url(r'^', include('inicio.urls'), name="inicio"),
    url(r'^api/', include('inicio.api.urls'), name="api"),

]


'''

curl -X POST -d "username=admin&password=password123" http://localhost:8000/api/auth/token

"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InBlcGVAaG90bWFpbC5jb20iLCJleHAiOjE1MDQxMTEzMjgsInVzZXJuYW1lIjoicGVwZSJ9.jUJkhcvUWzHIytMQLHOCpzARBRXqxf_0w-yWC43CcbU"

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6InBlcGVAaG90bWFpbC5jb20iLCJleHAiOjE1MDQxMTEzMjgsInVzZXJuYW1lIjoicGVwZSJ9.jUJkhcvUWzHIytMQLHOCpzARBRXqxf_0w-yWC43CcbU" http://localhost:8000/api/peliculas/


'''
