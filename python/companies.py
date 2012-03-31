from http import HTTP

class MyCompany(HTTP):
    url = 'mycompany.com'
MyCompany.get('projects', 'employees', 'customers')

class YourCompany(HTTP):
    url = 'yourcompany.com'
YourCompany.get('projects', 'employees')
