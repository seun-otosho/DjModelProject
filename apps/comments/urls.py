from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Comment", api.CommentViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("comments/Comment/", views.CommentListView.as_view(), name="comments_Comment_list"),
    path("comments/Comment/create/", views.CommentCreateView.as_view(), name="comments_Comment_create"),
    path("comments/Comment/detail/<int:pk>/", views.CommentDetailView.as_view(), name="comments_Comment_detail"),
    path("comments/Comment/update/<int:pk>/", views.CommentUpdateView.as_view(), name="comments_Comment_update"),
)
