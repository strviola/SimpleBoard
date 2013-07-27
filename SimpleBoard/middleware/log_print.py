'''
Created on 2013/07/25

@author: SuzukiRyota
'''


import logging


class PrintHeaderMiddleware(object):
    def _print_header(self, key):
        try:
            logging.warning('HEADER %s: %s' % (key, str(self.meta[key])))
        except KeyError:
            logging.warning('NOT FOUND: %s' % key)

    def _print_fav(self):
        self._print_header('REQUEST_METHOD')
        self._print_header('USER')
        self._print_header('HTTP_HOST')
        self._print_header('HTTP_USER_AGENT')
        self._print_header('HTTP_COOKIE')
        self._print_header('HTTP_REFERER')
        
    def _print_all(self):
        for k in self.meta:
            self._print_header(k)
        
    
    def process_view(self, request, callback, callback_args, callback_kwargs):
        self.meta = request.META

        self._print_fav()
        # self._print_all()

        return None
