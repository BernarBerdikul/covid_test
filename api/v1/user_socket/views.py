from django.shortcuts import render


def get_user_socket(request):
    return render(request, "api/user_socket.html")
