from styles.models import Style
from .models import School


def school_contacts(request):
    school_queryset = School.objects.all()
    context = dict()
    if school_queryset and hasattr(school_queryset[0], 'contact'):
        contacts = school_queryset[0].contact
        context = {
            'school': contacts.school.title,
            'country': contacts.country,
            'city': contacts.city,
            'street': contacts.street,
            'postcode': contacts.postcode,
            'phones': contacts.phones.split(','),
        }

    return {'contacts': context}


def styles_list(request):
    queryset_list = Style.objects.filter(sub_style__isnull=True).order_by(
        'order')
    return {'styles': queryset_list}
