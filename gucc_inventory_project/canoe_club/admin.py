from django.contrib import admin
from canoe_club.models import UserProfile, User
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user',)

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        return queryset

    user_info.short_description = 'Info'
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username","email"]
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User,UserAdmin)

