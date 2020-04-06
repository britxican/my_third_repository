#!/usr/bin/python3

import pdb
# Used in sendRequest and sendRequestUsingNextPageInfo
import requests

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# myCoolFunction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def MyCoolFunction(query, accstkn, \
        perPageParam = 100, \
        orderParam = 'asc', \
        quals = 'in:file'):

    URL = 'https://api.laCucarachaReloaded.com/search/?q=' + \
        '%22' + query + '%22' + '+' + quals + params 
    
    hdrs = {}
    hdrs['Authorization'] = 'token ' + accstkn
