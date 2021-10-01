from django.dispatch import receiver
from django.http import request
from app.models import TodoModel
from django.db.models.signals import post_delete
from django.contrib import messages


@receiver(post_delete, sender=TodoModel)
def delete_msg(sender, instance, **kwargs):
    if instance:
        print('deleting ...', instance.id, request)
