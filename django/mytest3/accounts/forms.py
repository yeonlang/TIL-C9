from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

# Create your models here.
class ChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username',]