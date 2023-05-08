init python:
    from inspect import getargspec
    config.debug = True
    config.developer = True

    def scan_(s, *types):
        for k, v in globals().items():
            if (
                s.lower() in k.lower()
                # and (not exclude or not isinstance(v, exclude))
                and (not types or isinstance(v, types))
            ):
                yield k, v

    def l_(s, *types):
        results = list(scan_(s, *types))
        width = max(map(lambda (k, v): len(k), results or [('', None)]))
        print "-", s, types, "found", len(results), "----------------"
        for k, v in results:
            print k.ljust(width), v_(v)
        print "Done."

    def v_(v):
        if callable(v):
            try:
                return getargspec(v)
            except Exception as e:
                return repr(v) + " -- Exception: " + repr(e)
        return repr(v)
