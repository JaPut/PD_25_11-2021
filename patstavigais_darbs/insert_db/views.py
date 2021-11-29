from django.shortcuts import render

from .models import User
from .forms import CreateUserForm, FilterUserForm

def filter(request):

    form = FilterUserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user_name = form.cleaned_data['username']
            users = User.objects.filter(username=user_name)

            context = {
                'users': users,
            }

            return render(
                request,
                template_name='users.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='filter_user.html',
        context=context,
    )

def filters(request):

    if request.method == 'POST':

        user_name = request.POST.get("users", "")
        users = User.objects.filter(username=user_name)

        context = {
            'users': users,
        }

        return render(
            request,
            template_name='users.html',
            context=context,
        )



    return render(
        request,
        template_name='usershtml.html',

    )


def get_visit(request, visit_id):

    user = User.objects.get(id=visit_id)

    context = {
        'user': user,
    }

    return render(
        request,
        template_name='user.html',
        context=context,
    )


def get_users(request):

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(
        request,
        template_name='users.html',
        context=context,
    )


def add_user(request):

    form = CreateUserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = User(
                username=form.cleaned_data['username'],
                e_mail=form.cleaned_data['e_mail'],
                reason=form.cleaned_data['Reason'],
            )

            user.save()

            context = {
                'user': user,
            }

            return render(
                request,
                template_name='user.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_user.html',
        context=context,
    )