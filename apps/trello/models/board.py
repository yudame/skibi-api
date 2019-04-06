import uuid
from datetime import datetime

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from apps.trello.models.abstract import TrelloObject


class Board(TrelloObject):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, null=False)
    is_closed = models.BooleanField(default=False)

    # MODEL PROPERTIES

    @property
    def short_url(self):
        return f"https://trello.com/b/{self.trello_shortlink}"

    # MODEL FUNCTIONS


# reset all board details
@receiver(pre_save, sender=Board)
def pre_save(instance, *args, **kwargs):
    from apps.trello.trello import client
    t_board = client.get_board(instance.trello_id)
    instance.trello_id = t_board.id
    instance.trello_url = t_board.url
    instance.name = t_board.name
    instance.is_closed = t_board.closed


# load board and make blog, populate lists, and labels (in that order_
@receiver(post_save, sender=Board)
def post_save(instance, *args, **kwargs):
    if instance.is_closed:
        try:
            instance.blog.unpublished_at = datetime.now()
            instance.blog.save()
        except:
            pass
    else:
        from apps.trello.models.list import List
        from apps.trello.models.label import Label
        from apps.blog.models import Blog
        from apps.trello.trello import client
        t_board = client.get_board(instance.trello_id)
        t_board.trello_id = t_board.id


        blog, created = Blog.objects.get_or_create(
            trello_board = instance
        )

        t_labels = t_board.get_labels()
        for t_label in t_labels:
            if t_label.name:
                label, created = Label.objects.get_or_create(
                    trello_id=t_label.id,
                    board=instance,
                    name=t_label.name,
                    color=t_label.color,
                )

        t_lists = t_board.open_lists()
        for t_list in t_lists:
            if 'PUBLISH' in t_list.name.upper() or 'DRAFT' in t_list.name.upper():
                list, created = List.objects.get_or_create(
                    trello_id=t_list.id,
                    board=instance,
                    name=t_list.name,
                    position=t_list.pos,
                    is_closed=t_list.closed
                )