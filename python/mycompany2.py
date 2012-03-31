
class MyCompany(object):
    '''
    Let access different entities of mycompany.com
    '''

    url = 'mycompany.com'

def make_get(path):
    '''
    Return a new function in charge of retrieving the entity specified in path
    '''
    def actual_get(self):
        return 'GET ' + self.url + '/' + path

    return actual_get

# For each name in the list, add a new class method
for name in ['projects', 'employees', 'customers', 'products']:
    setattr(MyCompany, name, make_get(name))
