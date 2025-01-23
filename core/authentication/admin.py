from django.contrib import admin

from core.authentication.models import User, Student, Office, GuildMemberData

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Office)
admin.site.register(GuildMemberData)