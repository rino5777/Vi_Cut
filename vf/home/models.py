from django.db import models

# Create your models here.
class VideoForm(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=False, max_length=30, blank=True)
    video = models.FileField(  blank=True,null=True)
    #name = models.CharField(max_length=100, db_index=True)

    

    def __str__(self):
        return str(self.video)