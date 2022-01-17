from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from user.models import CasinoUser
from user.api.serializers import CasinoUserSerializer

#---------------------------------------------------------------------------------------------------------
# Api Requests for user.models.CasinoUser
#---------------------------------------------------------------------------------------------------------

@api_view(['POST', ])
def registration_view(request):
    ''' Registration of CasinoUser -> Player '''
    serializer = CasinoUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registration Successfull"})
    else:
        return Response(serializer.errors)

@api_view(['PUT', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def update_view(request, pk):
    ''' Updation of CasinoUser -> Player '''
    try:
        casinoUser = CasinoUser.objects.get(email=pk)
    except CasinoUser.DoesNotExist:
        return Response({"error": "User Does Not Exist"})

    serializer = CasinoUserSerializer(instance=casinoUser, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Updated Successfully'}) 
    else:
        return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def deposit_view(request, pk):
    ''' Updation of CasinoUser -> Player '''
    try:
        casinoUser = CasinoUser.objects.get(email=pk)
    except CasinoUser.DoesNotExist:
        return Response({"error": "User Does Not Exist"})

    serializer = CasinoUserSerializer(instance=casinoUser, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.deposit(casinoUser, request.data['amount'])
        return Response({'message': 'Deposited Successfully'}) 
    else:
        return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def withdraw_view(request, pk):
    ''' Updation of CasinoUser -> Player '''
    try:
        casinoUser = CasinoUser.objects.get(email=pk)
    except CasinoUser.DoesNotExist:
        return Response({"error": "User Does Not Exist"})

    serializer = CasinoUserSerializer(instance=casinoUser, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.withdraw(casinoUser, request.data['amount'])
        return Response({'message': 'Withdrawal Successfully'}) 
    else:
        return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def transfer_view(request, pk1, pk2):
    ''' Transfer Funds CasinoUser -> Player '''
    try:
        casinoUser1 = CasinoUser.objects.get(email=pk1)
        casinoUser2 = CasinoUser.objects.get(email=pk2)
    except CasinoUser.DoesNotExist:
        return Response({"error": "User Does Not Exist"})

    serializer = CasinoUserSerializer(instance=casinoUser1, data=request.data, partial=True)
    serializer = CasinoUserSerializer(instance=casinoUser2, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.withdraw(casinoUser1, request.data['amount'])
        serializer.deposit(casinoUser2, request.data['amount'])
        return Response({'message': 'Transfer Successful'}) 
    else:
        return Response(serializer.errors)


@api_view(['DELETE', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def delete_view(request, pk):
    ''' Deletion of CasinoUser -> Player '''
    try:
        CasinoUser.objects.get(email=pk)
    except CasinoUser.DoesNotExist:
        return Response({"message": "User Does Not Exist"})

    user_delete = CasinoUser.objects.get(email=pk)
    user_delete.delete()

    return Response({"message": "Deleted Successfully"})

@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def user_view(request, pk):
    ''' View of CasinoUser -> Player '''
    try:
        casinoUser = CasinoUser.objects.get(email=pk)
        serializer = CasinoUserSerializer(casinoUser, many=False)
    except CasinoUser.DoesNotExist:
        return Response({"message": "user not found"})
    
    return Response(serializer.data)