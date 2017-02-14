import os

from django.conf import settings
def handle_uploaded_file(f,name):
    root = settings.MEDIA_ROOT + '/Publicaciones/' + name
    with open(root, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return root