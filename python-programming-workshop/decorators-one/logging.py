import functools

def log(logger, level='info'):
    def log_decorator(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kwa):
            getattr(logger, level)(fn.__name__)
            return fn(*a, **kwa)
        return wrapper
    return log_decorator

# later that day ...
@log(logging.getLogger('main'), level='warning')
def potentially_dangerous_function(times):
    for _ in xrange(times): rockets.get_rocket(NUCLEAR=True).fire()
