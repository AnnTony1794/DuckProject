from .models import Blog


def posts(request):
    return {
        'posts': Blog.objects.order_by('-created')[:3]
    }