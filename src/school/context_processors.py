from .models import School


def school_contacts(request):
    school_queryset = School.objects.all()
    if school_queryset:
        contacts = school_queryset[0].contact
    else:
        contacts = None
    context = {
        'school': contacts.school.title,
        'address': contacts.address.split(','),
        'phones': contacts.phones.split(','),
    }
    return {'contacts': context}
