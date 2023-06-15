from django.contrib.auth.models import User
from accounts.models import Profile
import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
setup()


def update_users():
    users = User.objects.all()
    for user in users:
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=user)
            profile.save()


if __name__ == "__main__":
    update_users()
