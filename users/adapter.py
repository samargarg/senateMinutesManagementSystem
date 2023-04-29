from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from rest_framework.authtoken.models import Token


class MyAccountAdapter(DefaultAccountAdapter):
    # def save_user(self, request, user, form, commit=True):
    #     print("FooAppAccountAdapter.save_user")
    #     return super(MyAccountAdapter, self).save_user(
    #         request, user, form, commit
    #     )

    def get_login_redirect_url(self, request):
        user = request.user
        print(user)
        token = Token.objects.get(user=user)
        if not token:
            token = Token.objects.create(user=user)
            token.save()
        print(token)
        path = f"/profile/?token={token}"
        return path.format(username=request.user.username)


# class MyAccountSocialAdapter(DefaultSocialAccountAdapter):
#     def save_user(self, request, sociallogin, form=None):
#         print("FooAppSocialAccountAdapter.save_user")
#         return super(MyAccountSocialAdapter, self).save_user(
#             request, sociallogin, form
#         )
