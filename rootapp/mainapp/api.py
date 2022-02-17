

from rest_framework import routers
from api import api_views as rental_views

router = routers.DefaultRouter()
router.register('friends', rental_views.FriendViewSet)
router.register('belongings', rental_views.BelongingViewSet)
router.register('borrowings', rental_views.BorrowedViewSet)