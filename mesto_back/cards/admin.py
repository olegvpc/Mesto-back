from django.contrib import admin
from .models import User, Card, Like

class CardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'likes_list', 'owner', 'createdAt')

    def likes_list(self, obj):
        return "\n".join([a.name for a in obj.likes.all()])


# class OwnerAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name', '_id')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'card', 'user')


admin.site.register(Card, CardAdmin)
# admin.site.register(Owner, OwnerAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(User)
