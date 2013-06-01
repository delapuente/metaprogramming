class HTTP(object):
    '''
    Let dynamic definition of GET methods.
    '''

    @classmethod
    def get(cls, *names):
        '''
        Add new GET methods to the class. One by argument received.
        '''

        def make_get(path):
            def actual_get(self):
                return 'GET ' + self.url + '/' + path

            return actual_get

        for name in names:
            setattr(cls, name, make_get(name))


    def __getattr__(self, name):
        '''
        Override regular attribute access to check for existence of the
        attribute. If not, it provides a default GET method by calling class
        method HTTP.get() with the name of the attribute being retrieved.
        '''

        HTTP.get(name)
        return getattr(self, name)
