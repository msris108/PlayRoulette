from rest_framework import serializers
from roulette.models import RouletteGame, RouletteBet, RouletteNumber

class RouletteGameSerializer(serializers.ModelSerializer):
    ''' Serializer of roulette.model.RouletteGame '''
    class Meta:
        model = RouletteGame
        fields = '__all__'

    def activate(self, instance):
        ''' Method to activate the games -> Admin Usages '''
        instance.is_active = True
        instance.save()

    def deactivate(self, instance):
        ''' Method to activate the games -> Admin Usages '''
        instance.is_active = False
        instance.save()

class RouletteNumberSerializer(serializers.ModelSerializer):
    ''' Serializer of roulette.model.RouletteNumber '''
    class Meta:
        model = RouletteNumber
        fields = '__all__'

class RouletteBetSerializer(serializers.ModelSerializer):
    ''' Serializer of roulette.model.RouletteBet '''
    class Meta:
        model = RouletteBet
        fields = '__all__'
    
    def activate(self, instance):
        ''' Method to activate the bets -> Admin Usages '''
        instance.is_active = True
        instance.save()

    def deactivate(self, instance):
        ''' Method to activate the bets -> Admin Usages '''
        instance.is_active = False
        instance.save()
