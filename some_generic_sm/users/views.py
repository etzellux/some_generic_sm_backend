from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.forms import ValidationError

from some_generic_sm.users.models import User
from some_generic_sm.users.forms import UserSignInForm, UserSignUpForm


class SignUpView(View):
    template_name = 'users/user_signup.html'

    def get(self, request):
        form = UserSignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            login(request, user)

            return redirect('/')

        return render(request, self.template_name, {'form': form})


class SignInView(View):
    template_name = 'users/user_signin.html'

    def get(self, request):
        form = UserSignInForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(
                    field=form.username,
                    error=ValidationError('Invalid username or password.')
                )
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
