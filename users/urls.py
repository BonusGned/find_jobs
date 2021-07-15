from django.urls import path

from users.views import ResumeViewSet, UserBookmarkVacancyView, BookmarksListView, ResponsesListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'resume',  ResumeViewSet, basename='resume')
# router.register(r'resume//', ResumeViewSet, basename='resume_detail')
router.register(r'add_bookmarks', UserBookmarkVacancyView, basename='add_bookmarks')
router.register(r'bookmarks', BookmarksListView, basename='bookmarks')
router.register(r'responses', ResponsesListView, basename='responses')

# urlpatterns = router.urls


# urlpatterns = [
#     path('resume/', ResumeViewSet.as_view({'get': 'list'})),
#     path('resume/<slug:pk>/', ResumeViewSet.as_view({'get': 'retrieve'})),
#     path('add_bookmarks/<int:pk>/', UserBookmarkVacancyView.as_view({'put': 'update'})),
#     path('bookmarks/', BookmarksListView.as_view()),
#     path('responses/', ResponsesListView),
# ]
