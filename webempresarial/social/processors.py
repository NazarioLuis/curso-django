from .mymodels.link import Link

def ctx_dic(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.link
    return ctx