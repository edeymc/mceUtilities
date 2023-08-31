import pandas as pd
import numpy as np
import httpx
from time import sleep

now = lambda: pd.to_datetime('now',utc=True).value/1e9

def fetch(URL,auth=(),last=[0],delay=0.5,cache=None,expires=10):
    '''optionally cache and/or rate limit get requests'''
    refetch = False
    called = now()
    if cache:
        (created,modified,accessed),(status_code,content) = cache.fetch(URL)
        if expires > now-created:
            refetch = True
    else:
        refetch = True
    if not refetch:
        accessed = now
        cache.set(URL,((created,modified,accessed),(status_code,content)))
    return content
    delta = called-last[-1]
    if delta < delay:
        sleep(delay-delta)
    if refetch:
        if auth:
            req = httpx.get(URL,auth=auth)
        else:
            req = httpx.get(URL)
        fetched = now()
        if cache:
            if not created:
                created = fetched
            modified, accessed = fetched,fetched
            status_code,content = req.status_code,req.content
            cache.set(URL,((created,modified,accessed),(status_code,content)))
    return content

def t2f(S):
    if not(S or False):
        return None
    m,s = ('0:%s' % S).split(':')[-2:]
    return np.round(60*int(m) + float(s),2)

def f2t(S):
    if not(S or False) or (int(''.join([c for c in '0'+str(S) if c.isdigit()])) == 0):
        return ''
    S = float(S)
    m = int(S/60)
    s = S-60*m
    hs = s-int(s)
    s = int(s)
    return f'{m:02}:{s:02}.{round(hs*100):02}'

CSG = (
    pd.DataFrame([
        {'Stroke':'Butterfly','Distance':50,'SportClass':[1,2,3,4,5,6,7]},
        {'Stroke':'Butterfly','Distance':100,'SportClass':[8,9,10,11,12,13,14]},
        {'Stroke':'Backstroke','Distance':50,'SportClass':[1,2,3,4,5]},
        {'Stroke':'Backstroke','Distance':100,'SportClass':[1,2,6,7,8,9,10,11,12,13,14]},
        {'Stroke':'Breaststroke','Distance':50,'SportClass':[1,2,3]},
        {'Stroke':'Breaststroke','Distance':100,'SportClass':[4,5,6,7,8,9,11,12,13,14]},
        {'Stroke':'Freestyle','Distance':50,'SportClass':[1,2,3,4,5,6,7,8,9,10,11,12,13,14]},
        {'Stroke':'Freestyle','Distance':100,'SportClass':[1,2,3,4,5,6,7,8,9,10,11,12,13,14]},
        {'Stroke':'Freestyle','Distance':200,'SportClass':[1,2,3,4,5,14]},
        {'Stroke':'Freestyle','Distance':400,'SportClass':[6,7,8,9,10,11,12,13]},
        {'Stroke':'Medley','Distance':150,'SportClass':[1,2,3,4]},
        {'Stroke':'Medley','Distance':200,'SportClass':[5,6,7,8,9,10,11,12,13,14]},
    ])
    .explode('SportClass')
    .reset_index(drop=True)
)

wps_event_regex = r"'s (?P<Distance>[0-9]+) m (Individual )*(?P<Stroke>[a-zA-Z]+) [SBM]+(?P<SportClass>[0-9]+)"

