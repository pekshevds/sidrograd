# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from wish_list_app.services import (
    fetch_users_wish_list,
    add_to_wish_list,
    delete_from_wish_list,
    clear_wish_list
)
from catalog_app.models import Good


class WishListView(LoginRequiredMixin, View):

    # login_url = "/login/"
    # redirect_field_name = "redirect_to"

    def get(self, request):
        context = {"wish_list": fetch_users_wish_list(request.user)}
        return render(
            request,
            template_name="wish_list_app/index.html",
            context=context
        )


class WishListAddView(LoginRequiredMixin, View):
    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("id", 0))
        add_to_wish_list(user=request.user, good=good)

        context = {"wish_list": fetch_users_wish_list(request.user)}
        return render(
            request,
            template_name="wish_list_app/index.html",
            context=context
        )


class WishListDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("id", 0))
        delete_from_wish_list(user=request.user, good=good)

        context = {"wish_list": fetch_users_wish_list(request.user)}
        return render(
            request,
            template_name="wish_list_app/index.html",
            context=context
        )


class WishListClearView(LoginRequiredMixin, View):
    def get(self, request):
        clear_wish_list(user=request.user)

        context = {"wish_list": fetch_users_wish_list(request.user)}
        return render(
            request,
            template_name="wish_list_app/index.html",
            context=context
        )
