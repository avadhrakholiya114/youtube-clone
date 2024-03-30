from django.shortcuts import render, HttpResponse
from .models import Video, Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channel.models import *


# Create your views here.
# avadh114 123
def index(request):
    video = Video.objects.filter(visibility='public');

    context = {
        "video": video
    }
    return render(request, 'index.html', context)


def detail(request, id):
    video = Video.objects.get(id=id)

    # when ever this url hit add 1 view
    video.views = video.views + 1
    video.save()

    # getting all commment releted to video

    comment = Comment.objects.filter(video=video, active=True).order_by("-date")
    comment_count = comment.count()
    channel = Channel.objects.get(id=video.user.id)
    context = {
        "video": video,
        "comment": comment,
        "comment_count": comment_count,
        "channel": channel
    }
    return render(request, 'video.html', context)


def save_comment(request):
    if request.method == "POST":
        pk = request.POST.get("id")
        comment = request.POST.get("comment")
        video = Video.objects.get(id=pk)
        user = request.user
        comment = Comment.objects.create(comment=comment, user=user, video=video)
        comment.save()

        response = "done"
        return HttpResponse(response)

    # Cross
    # Site
    # Request
    # Forgery(CSRF)
    # delete_comment view is marked with @ csrf_exempt.This means that CSRF protection will not be applied to this view.


@csrf_exempt
def delete_comment(request):
    if request.method == 'POST':
        id = request.POST.get("cid")
        comment = Comment.objects.get(id=id)
        comment.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 2})


from django.http import JsonResponse

def new_subscriber(request, id):
    subscriber = Channel.objects.get(id=id)
    user = request.user

    if user in subscriber.subscriber.all():
        # remove because user is already there
        subscriber.subscriber.remove(user)
        response = "subscribe"
    else:
        subscriber.subscriber.add(user)
        response = "unsubscribe"

    return JsonResponse({'response': response})


def load_sub(request, id):
    subscriber = Channel.objects.get(id=id)
    sub_list = list(subscriber.subscriber.values())
    return JsonResponse({'subscribers': sub_list})

