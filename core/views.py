from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def listing(request):
    return render(request, "core/listing.html", {
        "blogs": Blog.objects.all()
    })

def view_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, "core/view_blog.html", {
        "blog": blog,
    })

def see_request(request):
    text = f"""
        Some attributes of the HttpRequset object:
        
        scheme: {request.scheme}
        path: {request.path}
        method: {request.method}
        GET: {request.GET}
        user: {request.user}
    """
    return HttpResponse(text, content_type="text/plain")

def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:
        
        username: {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff: {request.user.is_staff}
        is_supervisor: {request.user.is_superuser}
        is_active: {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")
