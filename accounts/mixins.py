from django.shortcuts import redirect


# Здесь мы создаём собственные группы пользователей и даём им права
class AdminGroupRequired:
    redirect_url = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.gas_perms(
            [
                'products.add_product',
                'products.change_product',
                'products.delete_product',
            ]
        ):
            return super(AdminGroupRequired, self).dispatch(request, *args, **kwargs)

        return redirect(self.redirect_url)