from .models import School


def school_contacts(request):
    school_queryset = School.objects.all()
    context = dict()
    if school_queryset and hasattr(school_queryset[0], 'contact'):
        contacts = school_queryset[0].contact
        context = {
            'school': contacts.school.title,
            'address': contacts.address.split(','),
            'phones': contacts.phones.split(','),
        }

    return {'contacts': context}
