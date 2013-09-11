'''
Created on 2013/09/09

@author: SuzukiRyota
'''


import logging
import backends


def str_length(var_name):
    # TODO: receive var_name, stack to csv, and test
    
    def decorator(view_func):
        def wrapper(request):
            logging.warning('%s: %s' % (var_name, request.REQUEST[var_name]))
            
            str_list = backends.read_name(var_name)
            if len(str_list) < 10:
                # too few samples: return as it is
                return view_func(request)
            
            return view_func(request)
            
        return wrapper
    
    return decorator
