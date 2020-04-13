def responds_to(obj, message):
    m = getattr(obj, message, None)
    if m is None:
        return False
    else:
        return callable(m)
