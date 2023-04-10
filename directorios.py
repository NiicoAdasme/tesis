# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:29:32 2023

@author: Nico
"""

import os

with os.scandir(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\tkinter\csv') as entries:
    for entry in entries:
        #print(entry.name)Ñuble
        nombre, extension = os.path.splitext(entry)
        if 'indice_riesgo_hidrico_' in nombre:
            #print('el nombre del archivo python es: '+ os.path.basename(nombre))
            filename =nombre.split('_')
            print(filename[3])
