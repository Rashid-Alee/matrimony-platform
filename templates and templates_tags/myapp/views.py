from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    # read database
    # create contesxt var(dict)

    return render(request, "myapp/home.html")


def index(request):
    my_dic = {
        "pages": ["one", "two", "three", "four"],
        "courses": ["python", "django", "java", "c++"],
    }
    return render(request, "myapp/index.html", context=my_dic)
