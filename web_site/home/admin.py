from django.contrib import admin
from home.models import Setting,ContactMessage,Language,SettingLang
# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage)

admin.site.register(Language),
admin.site.register(SettingLang)