import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from users.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.count():
            for admin in settings.ADMINS:
                username, email = admin
                username = username.strip().replace(' ', '')
                logger.info(f'Create admin account for {email}')
                admin = User.objects.create_superuser(
                    email=email,
                    username=username,
                    password=settings.DEFAULT_ADMIN_PASSWORD
                )
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            logger.info(
                'Admin accounts can only be initialized if no Accounts exist')
