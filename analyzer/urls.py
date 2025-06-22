from django.urls import path
from . import views

app_name = 'analyzer'

urlpatterns = [
    path('', views.upload_document, name='upload_document'),
    path('chat/<int:doc_id>/', views.document_chat, name='chat'),
]
