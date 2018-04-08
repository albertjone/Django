from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def hello(request):
    return HttpResponse("Welcome to Home")

def display_meta(request):
    values = request.META
    print(values)
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,values[k]))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))
