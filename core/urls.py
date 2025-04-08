from django.urls import path
from core.views import home_view, post_detail_view, contact_view, register_view, login_view,logout_view

app_name = 'core'

urlpatterns = [
    path('', home_view, name='home_view'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
    path('contact/', contact_view, name='contact'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]