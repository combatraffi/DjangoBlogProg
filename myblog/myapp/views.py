from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import PostForm
from myapp.models import Post


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('list.html')
    context = {'posts': posts}
    print("CONTEXT: {}".format(context))
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


# Create your views here.
