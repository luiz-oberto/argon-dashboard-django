from .models import Detentor

def user_info(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_staff:
        try:
            detentor = Detentor.objects.get(username=request.user.username)
            uorg = detentor.uorgs.first()
            context['detentor_username'] = detentor.username
            context['uorg_codigo'] = uorg.codigo if uorg else '0'
            context['possui_uorg'] = True if uorg else False
        except Detentor.DoesNotExist:
            context['detentor_username'] = ''
            context['uorg_codigo'] = ''
            context['possui_uorg'] = False
    return context
