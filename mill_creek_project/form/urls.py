from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^choose_platform/$', views.choose_platform, name='choose_platform'),
	url(r'^choose_login/$', views.choose_login, name='choose_login'),
	url(r'^choose_login_type/$', views.choose_login_type, name='choose_login_type'),
	url(r'^choose_payment/$', views.choose_payment, name='choose_payment'),
	url(r'^choose_connection/$', views.choose_connection, name='choose_connection'),
	url(r'^choose_design/$', views.choose_design, name='choose_design'),
	url(r'^choose_device_functions/$', views.choose_device_functions, name='choose_device_functions'),
	url(r'^choose_additional_functions/$', views.choose_additional_functions, name='choose_additional_functions'),
	url(r'^choose_content_management/$', views.choose_content_management, name='choose_content_management'),
	url(r'^total_page/$', views.total_page, name='total_page'),
	url(r'^contact_form/$', views.contact_form, name='contact_form'),
	url(r'^startpage/$', views.startpage, name='startpage'),
	url(r'^endpage/$', views.endpage, name='endpage')
]