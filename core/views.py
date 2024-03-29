from django.shortcuts import render,HttpResponse
from .models import Video,Comment
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# avadh114 123
def index(request):
    video = Video.objects.filter(visibility='public');

    context={
        "video" : video
    }
    return render(request,'index.html',context)

def detail(request,id):
    video=Video.objects.get(id=id)

    # when ever this url hit add 1 view
    video.views= video.views+1
    video.save()

    #getting all commment releted to video

    comment=Comment.objects.filter(video=video,active=True).order_by("-date")
    comment_count = comment.count()

    context = {
        "video": video,
        "comment":comment,
        "comment_count": comment_count,
    }
    return render(request, 'video.html', context)

def save_comment(request):
    if request.method == "POST":
        pk=request.POST.get("id")
        comment = request.POST.get("comment")
        video=Video.objects.get(id=pk)
        user = request.user
        comment = Comment.objects.create(comment=comment, user=user, video=video)
        comment.save()

        response="done"
        return  HttpResponse(response)

@csrf_exempt
def delete_comment(request):
    if request.method =='POST' :
        id = request.POST.get("cid")
        comment = Comment.objects.get(id=id)
        comment.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 2})