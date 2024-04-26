from django.shortcuts import render



def Dog_page(request):
    return render(request, "dog.html")


def Home_page(request):
    return render(request, "index.html")


def Help_page(request):
    return render(request, "help.html")


def Form_page(request):
    return render(request, "form.html")