from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello")

def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    allcap = request.POST.get('allcap', 'off')
    nextlineremover = request.POST.get('nextlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        analysed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuations:
                analysed += char

        params = {"purpose": "Remove Punctuations", "analyse_text": analysed}
        djtext = analysed

    if allcap == 'on':
        analysed = ''
        for char in djtext:
            analysed += char.upper()

        params = {"purpose": "Capitalise all Text", "analyse_text": analysed}
        djtext = analysed

    if nextlineremover == 'on':
        analysed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed += char

        params = {"purpose": "Remove next Lines", "analyse_text": analysed}
        djtext = analysed

    if extraspaceremover == 'on':
        analysed = ''
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analysed += char

        params = {"purpose": "Remove Extra Space", "analyse_text": analysed}

    return render(request, 'analyse.html', params)
