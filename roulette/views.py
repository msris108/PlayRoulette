import random

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from user.models import CasinoUser
from user.api.serializers import CasinoUserSerializer
from roulette.models import RouletteGame, RouletteBet, RouletteNumber
from roulette.api.serializers import RouletteGameSerializer, RouletteBetSerializer, RouletteNumberSerializer

#---------------------------------------------------------------------------------------------------------
# Api Requests for roulette.models.RouletteGame
#---------------------------------------------------------------------------------------------------------

@api_view(['POST', ])
@permission_classes([permissions.IsAdminUser])
def create_game_view(request):
    ''' Create Roulette.RouletteGame '''
    gameSerializer = RouletteGameSerializer(data=request.data)
    # creating an instance of RouletteNumber(Encrypted) for every -> RouletteGame
    number = {
        "gameID" : request.data['gameID'],
        "number" : random.randint(0, 36)
    }
    numberSerializer = RouletteNumberSerializer(data=number)
    if gameSerializer.is_valid():
        gameSerializer.save()
        if numberSerializer.is_valid():
            numberSerializer.save()
        return Response({"message": "Game Creation Successfull"})
    else:
        return Response(gameSerializer.errors)


@api_view(['DELETE', ])
@permission_classes([permissions.IsAdminUser])
def remove_game_view(request, pk):
    ''' Remove Roulette.RouletteGame '''
    try:
        RouletteGame.objects.get(gameID=pk)
    except RouletteGame.DoesNotExist:
        return Response({"error": "Game Does Not Exist"})

    game_delete = RouletteGame.objects.get(gameID=pk)
    game_delete.delete()

@api_view(['PUT', ])
@permission_classes([permissions.IsAdminUser])
def update_game_view(request, pk):
    ''' Update Roulette.RouletteGame '''
    try:
        rouletteGame = RouletteGame.objects.get(gameID=pk)
    except RouletteGame.DoesNotExist:
        return Response({"error": "Game Does Not Exist"})

    serializer = RouletteGameSerializer(instance=rouletteGame, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Updated Successfully'}) 
    else:
        return Response(serializer.errors)

@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def game_view_one(request, pk):
    ''' List RouletteGame -> by gameID '''
    try:
        rouletteGame = RouletteGame.objects.get(gameID=pk)
    except RouletteGame.DoesNotExist:
        return Response({"error": "Game Does Not Exist"})
    rouletteGame = RouletteGame.objects.get(gameID=pk)
    serializer = RouletteGameSerializer(rouletteGame, many=False)
    return Response(serializer.data)

@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def game_view_all(request):
    ''' List RouletteGame -> all games '''
    rouletteGame = RouletteGame.objects.all()
    serializer = RouletteGameSerializer(rouletteGame, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
@permission_classes([permissions.IsAdminUser])
def activate_game_view(request, pk):
    ''' Activate game by gameID:gameID '''
    try:
        rouletteGame = RouletteGame.objects.get(gameID=pk)
    except RouletteGame.DoesNotExist:
        return Response({"error": "Game Does Not Exist"})

    serializer = RouletteGameSerializer(instance=rouletteGame, many=False)
    try:
        serializer.activate(rouletteGame)
        return Response({'message': 'Game Activated Successfully'}) 
    except:
        return Response({'message': 'Game Activation Failed'})

@api_view(['GET', ])
@permission_classes([permissions.IsAdminUser])
def deactivate_game_view(request, pk):
    ''' Deactivate game by gameID:gameID '''
    try:
        rouletteGame = RouletteGame.objects.get(gameID=pk)
    except RouletteGame.DoesNotExist:
        return Response({"error": "Game Does Not Exist"})

    serializer = RouletteGameSerializer(instance=rouletteGame, many=False)
    try:
        serializer.deactivate(rouletteGame)
        return Response({'message': 'Game Deactivated Successfully'}) 
    except:
        return Response({'message': 'Game Deactivation Failed'})

#---------------------------------------------------------------------------------------------------------
# Api Requests for roulette.models.RouletteGame
#---------------------------------------------------------------------------------------------------------

@api_view(['POST', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def create_bet_view(request):
    ''' Create Roulette.RouletteBet '''
    serializer = RouletteBetSerializer(data=request.data)
    if serializer.is_valid():
        amount = request.data['amount']
        playerID = request.data['playerID']
        gameID = request.data['gameID']

        rouletteGame = RouletteGame.objects.get(gameID=gameID)
        rouletteBet = RouletteBet.objects.filter(gameID=gameID)
        casinoUser = CasinoUser.objects.get(email=playerID)
        gameSerializer = RouletteGameSerializer(rouletteGame, many=False)
        betSerializer = RouletteBetSerializer(rouletteBet, many=True)
        userSerializer = CasinoUserSerializer(casinoUser, many=False)

        if userSerializer.data['balance'] >= amount:
            if gameSerializer.data['bet_limit'] > len(betSerializer.data):
                if gameSerializer.data['amount_limit'] >= amount:
                    if gameSerializer.data['is_active']:
                        serializer.save()
                    else:
                        return Response({"message": "Betting for this Game Has Closed"})
                    return Response({"message": "Betting Successfull"})
                else:
                    return Response({"message": "Betting Amount has exceeded Betting Limit"})
            else:
                return Response({"message": "Maximum Bets Reached"})
        else:
            return Response({"message": "Insufficient Balance"})

    else:
        return Response(serializer.errors)

@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def bet_view_all(request):
    ''' List Roulette.RouletteBet -> all games '''
    rouletteGame = RouletteBet.objects.all()
    serializer = RouletteBetSerializer(rouletteGame, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def bet_view_player(request, pk):
    ''' View of Roulette.RouletteBet -> by playerID '''
    rouletteGame = RouletteBet.objects.filter(playerID=pk)
    serializer = RouletteBetSerializer(rouletteGame, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def bet_view_dealer(request, pk):
    ''' View of Roulette.RouletteBet -> by dealerID '''
    rouletteGame = RouletteBet.objects.filter(dealerID=pk)
    serializer = RouletteBetSerializer(rouletteGame, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def bet_view_game(request, pk):
    ''' View of Roulette.RouletteBet -> by gameID '''
    rouletteBet = RouletteBet.objects.filter(gameID=pk)
    serializer = RouletteBetSerializer(rouletteBet, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
@permission_classes([permissions.IsAdminUser])
def activate_bet_view(request, pk):
    ''' Activate bet by betID:id '''
    try:
        rouletteBet = RouletteBet.objects.get(id=pk)
    except RouletteBet.DoesNotExist:
        return Response({"error": "Bet Does Not Exist"})

    serializer = RouletteBetSerializer(instance=rouletteBet, many=False)
    try:
        serializer.activate(rouletteBet)
        return Response({'message': 'Bet Activated Successfully'}) 
    except:
        return Response({'message': 'Bet Activation Failed'})

@api_view(['GET', ])
@permission_classes([permissions.IsAdminUser])
def deactivate_bet_view(request, pk):
    ''' Deactivate bet by betID:id '''
    try:
        rouletteBet = RouletteBet.objects.get(id=pk)
    except RouletteBet.DoesNotExist:
        return Response({"error": "Bet Does Not Exist"})

    serializer = RouletteBetSerializer(instance=rouletteBet, many=False)
    try:
        serializer.deactivate(rouletteBet)
        return Response({'message': 'Bet Deactivated Successfully'}) 
    except:
        return Response({'message': 'Bet Deactivation Failed'})

@api_view(['GET', ])
@permission_classes([permissions.IsAdminUser])
def resolve_bets_view(request):
    ''' Resolves all active transactions, i.e., bets (roulette.RouletteBet) '''
    rouletteBet = RouletteBet.objects.filter(is_active=True)
    betSerializer = RouletteBetSerializer(rouletteBet, many=True)

    game_ids = set()
    for bet in betSerializer.data:
        betID = bet['id']
        dealerID = bet['dealerID']
        playerID = bet['playerID']
        gameID = bet['gameID']
        amount = bet['amount']

        rouletteNumber = RouletteNumber.objects.get(gameID=gameID)
        rouletteBet = RouletteBet.objects.get(id=betID)
        dealer = CasinoUser.objects.get(email=dealerID)
        player = CasinoUser.objects.get(email=playerID)

        gameSerializer = RouletteNumberSerializer(rouletteNumber, many=False)
        betUpdateSerializer = RouletteBetSerializer(rouletteBet, many=False)
        dealerSerializer = CasinoUserSerializer(dealer, many=False)
        playerSerializer = CasinoUserSerializer(player, many=False)

        if gameSerializer['number'] != bet['bet_number']:
            dealerSerializer.deposit(dealer, amount)
            playerSerializer.withdraw(player, amount)
        else:
            dealerSerializer.withdraw(dealer, amount)
            playerSerializer.deposit(player, amount)

        betUpdateSerializer.deactivate(rouletteBet)
        game_ids.add(gameID)

    for game_id in game_ids:
        rouletteGame = RouletteGame.objects.get(gameID=game_id)
        gameSerializer = RouletteBetSerializer(rouletteGame, many=False)
        gameSerializer.deactivate(rouletteGame)

    return Response({"message" : "All Active Bets Resolved"})


@api_view(['GET', ])
@permission_classes([permissions.IsAdminUser])
def resolve_bets_game_view(request, pk):
    ''' Resolves all active transactions -> by gameID, i.e., bets (roulette.RouletteBet) '''
    rouletteBet = RouletteBet.objects.filter(is_active=True, gameID=pk)
    betSerializer = RouletteBetSerializer(rouletteBet, many=True)

    for bet in betSerializer.data:
        betID = bet['id']
        dealerID = bet['dealerID']
        playerID = bet['playerID']
        gameID = bet['gameID']
        amount = bet['amount']

        rouletteNumber = RouletteNumber.objects.get(gameID=gameID)
        rouletteBet = RouletteBet.objects.get(id=betID)
        dealer = CasinoUser.objects.get(email=dealerID)
        player = CasinoUser.objects.get(email=playerID)

        gameSerializer = RouletteNumberSerializer(rouletteNumber, many=False)
        betUpdateSerializer = RouletteBetSerializer(rouletteBet, many=False)
        dealerSerializer = CasinoUserSerializer(dealer, many=False)
        playerSerializer = CasinoUserSerializer(player, many=False)

        if gameSerializer['number'] != bet['bet_number']:
            dealerSerializer.deposit(dealer, amount)
            playerSerializer.withdraw(player, amount)
        else:
            dealerSerializer.withdraw(dealer, amount)
            playerSerializer.deposit(player, amount)

        betUpdateSerializer.deactivate(rouletteBet)

    rouletteGame = RouletteGame.objects.get(gameID=pk)
    gameSerializer = RouletteBetSerializer(rouletteGame, many=False)
    gameSerializer.deactivate(rouletteGame)

    return Response({"message" : "All Active Bets Resolved"})