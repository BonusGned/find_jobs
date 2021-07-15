from users.views import ResumeViewSet, UserBookmarkVacancyView, BookmarksListView, ResponsesListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'resume',  ResumeViewSet, basename='resume')
router.register(r'add_bookmark', UserBookmarkVacancyView, basename='add_bookmarks')
router.register(r'bookmark', BookmarksListView, basename='bookmarks')
router.register(r'response', ResponsesListView, basename='responses')
