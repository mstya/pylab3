from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.note_list, name='note_list'),
    url(r'^note/(?P<pk>[0-9]+)/$', views.note_detail, name='note_detail'),
    url(r'^note/new/$', views.add_new, name='add_new'),
    url(r'^note/(?P<pk>[0-9]+)/edit/$', views.note_edit, name='note_edit'),
    url(r'^note/(?P<pk>[0-9]+)/delete/$', views.note_delete, name='note_delete')
]