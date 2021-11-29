from django.forms import (
    Form,
    CharField,
    EmailField,
    FileField,
)


class CreateUserForm(Form):

    username = CharField()
    e_mail = EmailField()
    Reason = CharField()

class FilterUserForm(Form):
    username = CharField()

class UploadCsvForm(Form):
    csv_file = FileField()
