from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashborad(request):
    return render(request, 'dashboard/dashborad.html'),
