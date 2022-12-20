from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self , phone_number , email , firstname , lastname,password):
        if not phone_number:
            raise ValueError('user must have Phone Number')
        if not email:
            raise ValueError('user must have Email')
        if not firstname:
            raise ValueError('user must have Firstname')
        if not lastname:
            raise ValueError('user must have Lastname')
        user = self.model(phone_number= phone_number , email = self.normalize_email(email) , firstname = firstname , lastname= lastname)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self):
        pass