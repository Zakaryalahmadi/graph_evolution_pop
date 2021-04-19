#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:42:56 2021

@author: lahmadi
"""

def lireDonnee(nom_fichier):
    table = []
    fData = open(nom_fichier)

    while True:
        line = fData.readline().replace(" ", "").replace("'", "")
        if line == "":
            break
        line = line[:-1] # supprimer le '\n'
        
        q = float(line) 
        
        table.append(q)
    fData.close()
    return table


def year_interval(annee_debut, annee_fin):
    list_annee = []
    annee = annee_debut
    for x in range(annee_fin - annee_debut):
        list_annee.append(annee)
        annee += 1
    return list_annee
      