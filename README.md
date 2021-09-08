# QuickDjango

Learn to build an online movie website by using django web framework.
- django 3.1.3
- bootstrap 4

## GetStarted

Create a Virutal Environment /venv for a movieapp
- understand what is a venv, how to setup it
- create a django project with a new quickdjang

```bash
#comand to create Virtual environment
python -m venv venv_quickdjango
#activate a created Virtual environment
venv_quickdjango\Scripts\activate
#Install django 3.1.3
pip install django==3.1.3
#Check the libraries
pip freeze
#Create a djang project
django-admin startproject quickdjango
#add the movieapp in the setting of the quickdjango

#create a movieapp
python manage.py startapp movieapp
INSTALLED_APPS = [
    '...',
    'movieapp'
]
#run the webserver
python manage.py runserver
#run http://127.0.0.1:8000/
```
## Create a movie app home page
```python
#Add a home function in a views.py
def home(request):
  return render(request, 'home.html', {})
#Add urls in the quickdjango
from [django app] import views
urlpatterns = [
    path('', views.home, name='home')
]
#Add a home.html in templates folder of movieapp
```
##Django Dashboard
```python
#command to intialize the Django dashboard
python manage.py migrate 
#Create a supper user
python manage.py createsuperuser (Ben21/pASSWRD)
#pythonmanage run server
http://127.0.0.1:8080/admin
```
## Use bootstrap4
go to https://getbootstrap.com/docs/5.1/getting-started/introduction/
copy the css into the head of our html page
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
```
copy js into the body of ourhtmlpage
```html
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
```

## Contributing
By ThanhTao, email at taothanh2020@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
