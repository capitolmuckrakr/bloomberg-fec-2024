from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('2020/', include('cycle_2020.urls', namespace='2020')),
    path('2022/', include('cycle_2022.urls', namespace='2022')),
    path('2024/', include('cycle_2024.urls', namespace='2024')),
    path('donor/', include('donor.urls', namespace='donor')),

]

urlpatterns += staticfiles_urlpatterns()
