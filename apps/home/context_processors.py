from .models import Detentor

def user_info(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_staff:
        try:
            detentor = Detentor.objects.get(username=request.user.username)
            uorg = detentor.uorgs.first()
            context['detentor_username'] = detentor.username
            context['uorg_codigo'] = uorg.codigo if uorg else ''
        except Detentor.DoesNotExist:
            context['detentor_username'] = ''
            context['uorg_codigo'] = ''
    return context