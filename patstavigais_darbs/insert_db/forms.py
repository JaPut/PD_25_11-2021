from django.forms import (
    Form,
    CharField,
    EmailField,
)


class CreateUserForm(Form):

    username = CharField()
    e_mail = EmailField()
    Reason = CharField()

class FilterUserForm(Form):
    username = CharField()