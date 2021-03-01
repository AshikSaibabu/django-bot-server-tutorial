from django.db import models


class ButtonCalls(models.Model):
    user = models.CharField(primary_key=True, max_length=50)
    fat_count = models.IntegerField(default=0)
    dumb_count = models.IntegerField(default=0)
    stupid_count = models.IntegerField(default=0)

    # class Meta:
    #     db_table = "button_call"
