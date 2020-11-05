from django.shortcuts import redirect, reverse
from rooms import models as room_models
from django.views.generic import TemplateView
from . import models as list_models


def toggle_room(request, room_pk):
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    # print(room)
    # print(type(room))
    action = request.GET.get("action", None)
    if room is not None and action is not None:
        # get_or_create => get은 하나만 가져옴
        the_list, _ = list_models.List.objects.get_or_create(
            user=request.user, name="My Favorite Houses"
        )
        if action == "add":
            the_list.rooms.add(room)
        elif action == "remove":
            the_list.rooms.remove(room)

    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))


class SeeFavsView(TemplateView):
    template_name = "lists/list_detail.html"

