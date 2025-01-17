from django.contrib import admin

from core.authentication.models import User
from core.authentication.models.guild_member import Office, GuildMember
from core.authentication.models.student import Student

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Office)
admin.site.register(GuildMember)