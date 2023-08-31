import pandas as pd

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

