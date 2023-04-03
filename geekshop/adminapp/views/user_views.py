from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from authapp.models import ShopUser
from authapp.forms import ShopUserRegisterForm
# from adminapp.forms
from django.urls import reverse

from geekshop.adminapp.forms import ShopUserAdminEditForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content = {
        'title': title,
        'objects': user_list
    }
    return render(request, 'adminapp/user.html', content)


def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()
    content = {'title': title, 'update_form': user_form}
    return render(request, 'adminapp/user_update.html')


def user_update(request, pk):
    title = 'пользователи/создание'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponse(reverse('admin:users', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/user_update.html', content)


def user_delete(request, pk):
    title = 'пользователи/создание'

    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponse(reverse('admin:users'))

    content = {'title': title, 'user_or_delete': user}
    return render(request, 'adminapp/user_delete.html', content)


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

