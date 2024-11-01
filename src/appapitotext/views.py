from django.http import HttpResponse
from django.conf import settings


def add_text(request):
    text = request.GET.get(settings.URL_PATH_FUNCTION_ADD_TEXT_VAR, '')
    with open(settings.FILE_DESTINATION, 'a') as file:
        file.write(text + '\n')
    return HttpResponse(f'Adding Text: {text}')
