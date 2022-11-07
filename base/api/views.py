from django.http import JsonResponse


def getRouters(request):
    routers = [
        'Get /api',
        'Get /api/room',
        'Get /api/room/:id',
    ]
    return JsonResponse(routers, safe=False)