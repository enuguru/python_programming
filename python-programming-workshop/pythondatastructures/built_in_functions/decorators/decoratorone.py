
from functools import wraps

def my_decorator(view_func):
    def _decorator(request, *args, **kwargs):
        # maybe do something before the view_func call
        response = view_func(request, *args, **kwargs)
        # maybe do something after the view_func call
        return response
    return wraps(view_func)(_decorator)

# how to use it...
def foo(request): return HttpResponse('...')
foo = my_decorator(foo)

# or...
@my_decorator
def foo(request): return HttpResponse('...')
