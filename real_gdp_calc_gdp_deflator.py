# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:50:59 2022

@author: maybe
"""
#get nominal GDP from user and return to function
def get_nom_gdp():
    nom_gdp = float(input("Enter Nominal GDP: "))
    return nom_gdp
#get real gdp from user and return to function
def get_real_gdp():
    real_gdp = float(input("Enter Real GDP: "))
    return real_gdp
                     
#perform gdp deflator calculation and then recalculate real gdp (returns the same number as initially entered for real gdp)
def real_gdp_calc():
    nom_gdp = get_nom_gdp()
    real_gdp = get_real_gdp()
    gdp_deflator_calc = (nom_gdp/real_gdp)
    real_gdp = nom_gdp/gdp_deflator_calc
    print(real_gdp)

real_gdp_calc()
