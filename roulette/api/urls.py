from django.urls import path
from roulette.views import (
    create_game_view,
    remove_game_view,
    update_game_view,
    game_view_one,
    game_view_all,
    create_bet_view,
    bet_view_all,
    bet_view_player,
    bet_view_dealer,
    bet_view_game,
    resolve_bets_view,
    activate_bet_view,
    deactivate_bet_view,
    resolve_bets_game_view,
    activate_game_view,
    deactivate_game_view,
)

''' Overview of the api urls '''

app_name = 'users'

urlpatterns = [
    path('create/', create_game_view, name="Create Game"),
    path('remove/', remove_game_view, name="Delete Game"),
    path('update/', update_game_view, name="Update Game"),
    path('activate/<str:pk>/', activate_game_view, name="Activation of Game"),
    path('deactivate/<str:pk>/', deactivate_game_view, name="Deactivation of Game"),
    path('view/', game_view_all, name="View All Games"),
    path('view/<str:pk>/', game_view_one, name="View Game By ID"),
    path('bet/create/', create_bet_view, name="Create Bet"),
    path('bet/', bet_view_all, name="View All Bets Placed"),
    path('bet/player/<str:pk>/', bet_view_player, name="View All bets of Player by PlayerID"),
    path('bet/dealer/<str:pk>/', bet_view_dealer, name="View All bets of Dealer by DealerID"),
    path('bet/game/<str:pk>/', bet_view_game, name="View All bets on a Game by GameID"),
    path('bet/activate/<str:pk>/', activate_bet_view, name="Activation of Bet"),
    path('bet/deactivate/<str:pk>/', deactivate_bet_view, name="Deactivation of Bet"),
    path('bet/resolve/', resolve_bets_view, name="Resolve all Active Bets"),
    path('bet/resolve/<str:pk>', resolve_bets_game_view, name="Resolve All Active Bets of a Game by GameID"),
]