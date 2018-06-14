from .models import SEO


def seo_optimisation(request):
    seo_queryset = SEO.objects.all()
    context = dict()
    if seo_queryset.exists():
        seo = seo_queryset.first()
        context = {
            'title': seo.title,
            'h1': seo.h1,
            'key_words': seo.key_words,
            'description': seo.description,
        }

    return {'seo': context}
