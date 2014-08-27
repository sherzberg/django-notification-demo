from django.http import HttpResponse

from notification import models as notification


def send(request):
    user = request.user

    notification.send_now(
        [user],
        'newsletters:new_newsletter',
        sender='backgroung-task:nightly-recalls',
        extra_context={'edition': '0001'}
    )

    return HttpResponse('OK')
