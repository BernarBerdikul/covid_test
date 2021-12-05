from django.shortcuts import render


def get_staff_socket(request):
    return render(request, "api/staff_socket.html")
