from rest_framework import serializers
from .models import Card, User, Like


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    name_user = serializers.CharField(source='name',
                                      )
    # user = UserSerializer()
    # user = serializers.SlugRelatedField(slug_field='name',
    #                                     queryset=User.objects.all()
    #                                     )


    class Meta:
        model = Like
        fields = ('name_user',)
        # fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True,
                           read_only=True
                           )
    owner = UserSerializer()

    class Meta:
        model = Card
        fields = ('likes', 'name', 'link', 'owner')
