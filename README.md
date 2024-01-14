# LittleLemon Cupcake Restaurant API

Welcome to the **LittleLemon Cupcake Restaurant API**! This Django REST API project is designed to provide cupcake information for the front end of the LittleLemon Cupcake Restaurant website. It offers a simple and efficient way to fetch menu items. This README will guide you through the setup and usage of the API.

## Getting Started
1-Install dependencies using Pipenv:
pipenv install
2-Activate the virtual environment:
pipenv shell
3-Apply database migrations:
python manage.py migrate
4-Run the development server:
python manage.py runserver

##API Endpoints
Menu Items

   + GET /api/menu-items/: Retrieve a list of all menu items.
   + GET /api/menu-items/{id}/: Retrieve details of a specific menu item by ID

### Frontend Integration
Integrate the API with your front end using the provided MenuItemsView and SingleMenuItemView. You can use the following example code:
### views.py

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

##Snapscreen


   ![screen-recorder-sun-jan-14-2024-17-33-38](https://github.com/Mu5alaf/LittleLemonAPI/assets/109148687/417db01e-6dc9-43d3-92c2-bf857e4a69e7)
 
