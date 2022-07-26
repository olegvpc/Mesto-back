from rest_framework import serializers
from .models import Card, User, Like


class UserSerializer(serializers.ModelSerializer):
    # поле cards добавили из связанной модельки Card
    # можно переопределить значение поля ответа - иначе будет Pk
    # name = serializers.SlugRelatedField(slug_field='username',
    #                                      many=True,
    #                                      queryset=User.objects.all())
    _id = serializers.CharField(source='id')

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('name', 'about', 'avatar', '_id', 'cohort')


class CardSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)  # выводит полный объект
    # важно - значение read_only=True делает поле owner не обязательным к
    # заполнению при записи в базу данных, полученных по API

    # при следущей сериализации данные берутся из модельки
    # __str__ - доступно только чтение
    # owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Card
        fields = ('likes', '_id', 'name', 'link', 'owner')
        # fields = '__all__'
        # read_only_fields = ('owner',)

    # def validate(self, data):
    #     print(data)
    #     if data['link'] == data['name']:
    #         raise serializers.ValidationError(
    #             'вот тот случай')
    #     return data
    # def validate(self, data):
    #     print(data)
    #     if data['link'] == data['name']:
    #         raise serializers.ValidationError(
    #             'вот тот случай')
    #     return data

    # def create(self, validated_data):
    #     # print(validated_data) #  все что пришло в POST API
    #     # print(self.initial_data['owner'])
    #     api_user = validated_data.pop('owner')
    #     id = self.initial_data['owner']['_id']
    #     card = Card.objects.create(**validated_data, owner_id=id)
    #     # print(card)
    #     # card.owner_id = self.initial_data['owner']['_id']
    #     # user = api_user['']
    #
    #     # print(self.initial_data['owner'])
    #     # print(self.initial_data['owner'])
    #     # api_user = self.initial_data['owner']
    #
    #     # {'owner': {'_id': 3, 'name': 'Third User', 'about': 'Painter',
    #     # 'avatar': None, 'cohort': None}, 'name': 'Picture API',
    #     # 'link': 'https://api.ru'}
    #
    #     # card.owner = User.objects.filter(_id=1)
    #     return card

#
# class LikeSerializer(serializers.ModelSerializer):
#     card = serializers.PrimaryKeyRelatedField(read_only=True)
#     user = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#         model = Like
#         # fields = '__all__'
#         fields = ('card', 'user')
