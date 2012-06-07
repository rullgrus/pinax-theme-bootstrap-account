from django.conf import settings

from appconf import AppConf


class ThemeAccountAppConf(AppConf):
    
    ADMIN_URL = "admin:index"
    
    class Meta:
        prefix = "theme_account"
