from .models import MainInfo


def main_info(request):
    context = {'info': ''}
    info = MainInfo.objects.all()
    if info.exists():
        info = info.first()
        context.update({'info': info})
    return context
