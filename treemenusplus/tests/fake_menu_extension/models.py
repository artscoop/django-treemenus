
from django.db import models
from treemenusplus.models import MenuItem

class FakeMenuItemExtension(models.Model):
    menu_item = models.OneToOneField (MenuItem, related_name="%(class)s_related")
    published = models.BooleanField(default=False)
