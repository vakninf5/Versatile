from django.shortcuts import render
# from django.shortcuts import HttpResponse

# def get_name(request, name):
#     if name is Nu:
#         name = "World"
#     return render(request, 'index.html')

def index(request):
    name = request.GET.get('name', 'world')
    return render(request, 'index.html', {'name': name})