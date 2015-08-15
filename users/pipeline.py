from social.pipeline.partial import partial

from users.models import UserProfile


@partial
def create_profile(backend, user, response, *args, **kwargs):
    if UserProfile.objects.filter(user=user).exists():
        profile = UserProfile.objects.get(user=user)
        return
    else:
        profile = UserProfile(user=user, city='', country='')
        profile.save()
        return
