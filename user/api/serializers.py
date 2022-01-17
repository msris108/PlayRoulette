from rest_framework import serializers
from user.models import CasinoUser

class CasinoUserSerializer(serializers.ModelSerializer):
    ''' Serializer for the CasinoUser Class '''
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CasinoUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        ''' Overriding the custom create method for the UserModel '''
        casinoUser = CasinoUser(
            email   = validated_data['email'],
            user_name = validated_data['user_name'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            balance = validated_data['balance']
        )

        password = validated_data['password']
        password_v = validated_data['password2']

        # Password Validation During User Creation
        if password != password_v:
            raise serializers.ValidationError({'message': 'Passwords Must Match'})

        casinoUser.set_password(password)
        casinoUser.save()

        return casinoUser

    def update(self, instance, validated_data):
        ''' Overriding the custom update method for the UserModel '''

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance 

    def deposit(self, instance, amount):
        ''' Helper Function to Deposit Funds '''
        instance.balance += amount
        instance.save()
        return instance  

    def withdraw(self, instance, amount):
        ''' Helper Function to Deposit Funds '''
        if instance.balance < amount:
            raise serializers.ValidationError({'message' : 'Withdrawal Amount less than Accout Balance'})
        instance.balance -= amount
        instance.save()
        return instance