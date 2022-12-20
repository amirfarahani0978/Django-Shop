from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, phone_number, firstname, lastname, password):
        if not phone_number:
            raise ValueError('user must have Phone Number')
        if not firstname:
            raise ValueError('user must have Firstname')
        if not lastname:
            raise ValueError('user must have Lastname')
        user = self.model(phone_number=phone_number,
                          firstname=firstname, lastname=lastname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, firstname, lastname, password):
        user = self.create_user(phone_number,
                                firstname, lastname, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
