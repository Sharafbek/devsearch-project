from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Skill


User = get_user_model()


class AddInputClass:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input input--text',
            })


class UserRegistrationForm(AddInputClass, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']



class SkillForm(AddInputClass, ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description'] 

    def __init__(self, *args, **kwargs):
        AddInputClass.__init__(self, *args, **kwargs)


class AccountForm(AddInputClass, ModelForm):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'user_permisssion', 'is_superuser', 'is_staff', 'groups', 'is_active', 'date_joined', 'bio', 'occupation']


