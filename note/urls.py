from django.conf.urls import url

from note.views import NoteUpdate
from . import views

urlpatterns = [
    url(r'^$', views.note_list, name='note_list'),
    url(r'^note/(?P<pk>[0-9]+)/$', views.note_detail, name='note_detail'),
    url(r'^note/new/$', views.add_new, name='add_new'),
    url(r'^note/edit/(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='note_edit'),
    url(r'^note/delete/(?P<pk>[0-9]+)/$', views.note_delete, name='note_delete')
]