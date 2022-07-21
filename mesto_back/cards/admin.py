from django.contrib import admin
from .models import Card, User, Like


class CardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'likes_list', 'createdAt')

    def likes_list(self, obj):
        return "\n".join([a.name for a in obj.likes.all()])


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', '_id')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'card', 'user')

admin.site.register(Card, CardAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Like, LikeAdmin)
