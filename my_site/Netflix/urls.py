from .views import (RegisterView,LogoutView,LoginView,UserProfileListAPIView,UserProfileDetailAPIView, CategoryListAPIView,CategoryDetailAPIView ,CountryListAPIView,
                    CountryDetailAPIView, GenreListAPIView,
                    GenreDetailAPIView, MovieListAPIView,MovieDetailAPIView,
                    DirectorListAPIView,DirectorDetailAPIView,ActorListAPIView,ActorDetailAPIView,
                    RatingViewSet,ReviewCreateAPIView,ReviewEditAPIView,ReviewLikeViewSet,FavoriteViewSet,
                    FavoriteMovieViewSet,HistoryMovieViewSet)
from rest_framework import routers
from django.urls import path,include


router = routers.SimpleRouter()

router.register(r'rating',RatingViewSet)
router.register(r'review_like',ReviewLikeViewSet)
router.register(r'favorite',FavoriteViewSet)
router.register(r'favorite_movie',FavoriteMovieViewSet)
router.register(r'history',HistoryMovieViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('review/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
]