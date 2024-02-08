App Name: Corporate Asset Tracker App

App Overview : Django app to track corporate assets such as phones, tablets, laptops 
and other gears handed out to employees.
Goals:
1.The application might be used by several companies
2.Each company might add all or some of its employees
3.Each company and its staff might delegate one or more devices to employees for
a certain period of time
4.Each company should be able to see when a Device was checked out and returned
Each device should have a log of what condition it was handed out and returned


Steps to run the project:

Clone the project from the git repository.
git clone https://github.com/MohammadIshak47/corporate_assets_tracker_app.git
Create a virtual environment and activate it.
Install the required packages from requirements.txt file.
Run the following commands:
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py loaddata datadb.json
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver


 the following url for performing API testing in swagger via a browser open:

url: http://127.0.0.1:8000/api/schema/swagger-ui/
Now, you can authenticate yourself before doing any operation. To do that, hit the token endpoint and pass the username and password in the body . Copy the access token and paste it in the authorize section of swagger. Now, you can perform any operation.
url: http://127.0.0.1:8000/token/
To login admin dashboard:
url: http://127.0.0.1:8000/admin/
