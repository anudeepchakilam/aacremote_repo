from django.shortcuts import render,get_object_or_404
from acc.forms import CommentForm
from acc.models import Comment
from django.views.generic import ListView
# Create your views here.
#class PostListView(ListView):

def post_detail_view(request):
    comments=Comment.objects.all()
    #comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'acc/home.html',{'form':form,'csubmit':csubmit,'comments':comments})
