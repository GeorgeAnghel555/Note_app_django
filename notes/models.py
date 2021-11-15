from django.db import models
import uuid


class Note(models.Model):
    level_importance=(('L','Low' ),
                      ('M', 'Medium'),
                      ('H','High'),)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    title = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    content = models.TextField(null=True,blank=True)
    importance = models.CharField(max_length = 1, choices = level_importance)

    def __str__(self):
        return self.title