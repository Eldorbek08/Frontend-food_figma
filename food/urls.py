from rest_framework.routers import DefaultRouter
from django.urls import path,include


from .views import CommentsViews,CategoryViews,foodsViews,BookTableViews,ContactViews

router = DefaultRouter()
router.register(r'Comments', CommentsViews, basename='CommentsViews')
router.register(r'Category', CategoryViews, basename='CategoryViews')
router.register(r'Foods', foodsViews, basename='foodsViews')
router.register(r'BookTable', BookTableViews, basename='BookTableViews')
router.register(r'Contact', ContactViews, basename='ContactViews')


urlpatterns = [
    path('', include(router.urls))
]
