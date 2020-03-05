from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from file.models import File

# Register your models here.
admin.site.register(
    File,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)