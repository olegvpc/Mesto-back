from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Card, User, Like
from .serializers import CardSerializer, UserSerializer

from rest_framework import mixins

from rest_framework import status
from rest_framework.decorators import api_view  # Импортировали декоратор
from rest_framework.response import Response


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        # print(self.request.user)
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return JsonResponse({'status': 'DELETED'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['PATCH', 'GET'])  # Добавили декоратор и указали разрешённые методы
def user_patch(request):
    current_user = User.objects.get(id=request.user.id)
    if request.method == 'PATCH':
        # print(request.user.id)
        # return Response(
        #     {'message': 'Получены обновленные данные',
        #      'data': request.data
        #       # 'user': current_user
        # })
        serializer = UserSerializer(current_user, data=request.data,
                                    partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = UserSerializer(current_user)
        return Response(serializer.data)
    # Изменили ответ
    return Response({'message': 'Это был не PATCH-запрос!'})


@api_view(['PUT', 'DELETE'])  # Добавили декоратор и указали разрешённые методы
def like_card(request, card_id):
    # print(request.user.id, card_id)
    if request.method == 'PUT':
        if Like.objects.filter(user_id=request.user.id, card_id=card_id):
            return Response({'message': 'ERROR: NO-UNIQUE pair USER-CARD'})
        Like.objects.create(user_id=request.user.id, card_id=card_id)
        card = Card.objects.get(_id=card_id)
        serializer = CardSerializer(card)
        # return Response({'message': 'LIKE-CREATED'})
        return Response(serializer.data)
    if request.method == 'DELETE':
        try:
            like = Like.objects.get(user_id=request.user.id, card_id=card_id)
            like.delete()
            # return Response({'message': 'LIKE-DELETED'})
            card = Card.objects.get(_id=card_id)
            # print(card)
            serializer = CardSerializer(card)
            return Response(serializer.data)
        except ValueError:
            return Response({'message': 'ERROR-NO SUCH RECORD'})

    # user_id = request.user.id
    #
    # if request.method == 'PUT':
    #     print(user_id)
        # return Response(
        #     {'message': 'Получены обновленные данные',
        #      'data': request.data
        #       # 'user': current_user
        # })
        # serializer = LikeSerializer(data=request.data,
        #                             partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # if request.method == 'GET':
    #     serializer = UserSerializer(current_user)
    #     return Response(serializer.data)
    # # Изменили ответ
    # return Response({'message': 'Это был не PATCH-запрос!'})


# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     # permission_classes = (IsAuthorOrReadOnly,)
#
#     # def get_queryset(self):
#     #
#     #     like = get_object_or_404(Like, id=self.kwargs.get('card_id'))
#     #     print(like)
#     #     # return card.likes
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     # def update(self, request, *args, **kwargs):
#     #     pass
#
#     def perform_create(self, serializer): # method POST
#         card_id = self.kwargs.get('card_id')
#         print(self.request.user.username, card_id)
#         serializer.save(user_id=self.request.user.id, card_id=card_id)
#
#     def destroy(self, request, *args, **kwargs):
#         print(self.get_object())
        # try:
        #
        #     # instance = self.get_object()
        #     # self.perform_destroy(instance)
        # except Http404:
        #     pass
        # return JsonResponse({'status': 'LIKE DELETED'})