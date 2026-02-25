from django.http import HttpResponse


html = '''
    <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <title>Meus Carros</title>
        </head>
        <body>
            <h1>Meus Carros</h1>
        </body>
    </html>
'''

def  cars_view(request):
    return HttpResponse(html)
