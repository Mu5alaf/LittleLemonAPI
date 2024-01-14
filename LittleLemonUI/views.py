from django.shortcuts import render
import requests
# Create your views here.
def homeView(request):
    api_url='http://127.0.0.1:8000/api/menu-item'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
    except request.RequestException as e:
        data = {'error':f'request failed:{str(e)}'}
    return render(request,"LittleLemon/layout.html",{'response':data})