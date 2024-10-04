from django.urls import path
from core_app_root import views
urlpatterns = [
    path("render_activation_code/",views.render_activation_template,name="render_activation_code")
]
