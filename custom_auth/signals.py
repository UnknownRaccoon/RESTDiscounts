from custom_auth.models import Company, Profile


def create_user(sender, **kwargs):
    print(str(sender))
    user = kwargs["instance"]
    if kwargs["created"]:
        if user.is_company:
            Company.objects.create(user=user)
        else:
            Profile.objects.create(user=user)
