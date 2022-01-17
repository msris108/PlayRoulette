# from django_cryptography.fields import encrypt
from encrypted_fields.fields import EncryptedIntegerField

from django.db import models
from django.db.models.deletion import CASCADE
from user.models import CasinoUser

class RouletteGame(models.Model):
    ''' Each Roulette Game is defined by this class -> Contains the attributes of the game '''
    gameID          = models.CharField(max_length=10, unique=True, primary_key=True)
    dealerID        = models.ForeignKey(CasinoUser, related_name="dealerID", on_delete=CASCADE)
    start_time      = models.DateTimeField()
    end_time        = models.DateTimeField()
    is_active       = models.BooleanField()
    bet_limit       = models.IntegerField()
    amount_limit    = models.IntegerField()

class RouletteBet(models.Model):
    ''' Each Roulette Bet is defined by this class -> Associats the bets made each User with the Game '''
    gameID          = models.ForeignKey(RouletteGame, related_name="game", on_delete=CASCADE)
    dealerID        = models.ForeignKey(CasinoUser, related_name="dealer", on_delete=CASCADE)
    playerID        = models.ForeignKey(CasinoUser, related_name="player", on_delete=CASCADE)
    bet_number      = models.IntegerField()
    amount          = models.IntegerField()
    is_active       = models.BooleanField()

class RouletteNumber(models.Model):
    gameID = models.ForeignKey(RouletteGame, related_name="GameID", on_delete=CASCADE)
    number = EncryptedIntegerField()


