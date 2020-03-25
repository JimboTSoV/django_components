from django.urls import path

from sandbox.pages.views import PageView, PageEditView

urlpatterns = [
    path("<uuid:pk>", PageView.as_view()),
    path("<uuid:pk>/edit", PageEditView.as_view(), name="page_via_id_edit"),
    path("<slug:slug>", PageView.as_view()),
    path("<slug:slug>/edit", PageEditView.as_view()),
    path("<path:path>/<slug:slug>", PageView.as_view()),
    path("<path:path>/<slug:slug>/edit", PageEditView.as_view(), name="page_via_path_edit"),
]