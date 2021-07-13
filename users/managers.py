from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')
        print(kwargs)
        user = self.model(email=self.normalize_email(email), location=kwargs.get('location'),
                          first_name=kwargs.get('first_name'),
                          last_name=kwargs.get('last_name'), phone_number=kwargs.get('phone'))

        user.set_password(password)

        user.save()
        return user

    # Create SuperUser
    def create_superuser(self, email, password, **kwargs):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email=email, password=password, location=kwargs.get('location'), first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'), phone_number=kwargs.get('phone')
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
