from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class File(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    is_file = models.BooleanField(default=False)

    def __str__(self):
        return self.name