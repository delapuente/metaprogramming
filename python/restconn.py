#!/usr/bin/python

class RESTConn(object):
  '''
  Instantiate using an entry point like foobar.com:
    c = RESTConn('foobar.com')

  Use methods like:
    c.get_from_articles(pubdate='20130101')
    c.post_to_polls({'title':'The Python programming language', 'body':'...'}).

  You need to always use an intermediate word between verb and conllection 
  unless you use __ (double underscore) to separate them:
    c.update__articles()
  '''

  def __init__(self, entry_point):
    self.entry_point = entry_point

  def method_builder(self, method_name):
    verb, _, collection = method_name.split('_', 2)
    def do_verb(payload=None, **kwargs):
      uri = self.make_uri(collection)
      querystring = self.make_querystring(kwargs)
      print verb.upper(), self.combine(uri, querystring)
      if payload:
        print payload

    return do_verb

  def make_uri(self, collection):
    return '/'.join([self.entry_point, collection])

  def make_querystring(self, kwargs):
    return '&'.join(['='.join(pair) for pair in kwargs.iteritems()])

  def combine(self, uri, querystring):
    if querystring:
      return '&'.join([uri, querystring])

    return uri

  def __getattr__(self, name):
    method = self.method_builder(name)
    setattr(self, name, method)
    return getattr(self, name)

