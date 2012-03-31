class MyCompany(object):
    '''
    Let access different entities of mycompany.com
    '''

    url = 'mycompany.com'

    def projects(self):
        return self._get('/projects')

    def employees(self):
        return self._get('/employees')

    def customers(self):
        return self._get('/customers')

    def products(self):
        return self._get('/products')

    def _get(self, path):
        return 'GET ' + self.url + path
