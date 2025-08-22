# notifications/utils.py
from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(*, recipient, actor, verb, target=None):
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_content_type=ContentType.objects.get_for_model(target) if target else None,
        target_object_id=getattr(target, "pk", None) if target else None,
    )
