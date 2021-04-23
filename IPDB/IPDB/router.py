from registrations.viewsets import UserViewset, PartyViewset, PoliticiansViewset, PartyRatingViewSet, PoliticianRatingViewSet, PoliticianWorkViewset,PoliticianWorkRatingViewSet
from rest_framework import routers
from registrations import views

router = routers.DefaultRouter()
router.register('users',UserViewset,basename='users')
router.register('parties',PartyViewset,basename='parties')
router.register('politicians',PoliticiansViewset,basename='politicians')
router.register('partyRating',PartyRatingViewSet,basename='partyRating')
router.register('politiciansRating',PoliticianRatingViewSet,basename='politiciansRating')
router.register('politiciansWork',PoliticianWorkViewset,basename='politiciansWork')
router.register('politiciansWorkRatings',PoliticianWorkRatingViewSet,basename='politiciansWorkRatings')



