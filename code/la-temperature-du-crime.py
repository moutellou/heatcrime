# -*- coding: utf-8 -*-
# date: 9 juillet 2019
# auteur: wesley campbell

import glob

file_list = glob.glob('./*.csv')

all_data = []

for name in file_list:
    
    if name == './temperature-data.csv':
        
        continue
    
    infile = open(name)
    readfile = infile.readlines()
    
    for i in range(len(readfile)):
        
        if "Date/Heure" in readfile[i]:
            
            start = i + 1
            break
    
    data = readfile[start:]
    
    for i in range(len(data)):
        
        data[i] = data[i].split()[1].split(',')
        
        heure = int(data[i][0].strip('"')[:-3])
        
        if heure == 0 or heure == 12 or heure == 18:
            
            annee  = int(data[i][1].strip('"'))
            mois = int(data[i][2].strip('"'))
            jour = int(data[i][3].strip('"'))
            
            try:
            
                temp = float(data[i][5].strip('"'))
            
            except IndexError:
                
                temp = 'nan'
            
            # assebmle the date
            if mois < 10 and jour < 10:
                
                date = str(annee)+'-0'+str(mois)+'-0'+str(jour)
                
            elif mois < 10 and jour >= 10:
                
                date = str(annee)+'-0'+str(mois)+'-'+str(jour)
                
            elif mois >= 10 and jour < 10:
                
                date = str(annee)+'-'+str(mois)+'-0'+str(jour)
                
            else:
                
                date = str(annee)+'-'+str(mois)+'-'+str(jour)
                
            # classify the time of day
            if heure == 0:
                
                heure = 'nuit'
                
            elif heure == 12:
                
                heure = 'jour'
                
            elif heure == 18:
                
                heure = 'soir'
            
            datum = (heure, date, temp)
            
            all_data.append(datum)
            
    infile.close()

def sortOne(val):
    
    return(val[1])
    
all_data.sort(key = sortOne)

newfile = open('temperature-data.csv', 'w')
newfile.write('Heure,Date,Temperature\n')

for value in all_data:
    
    newfile.write(str(value[0])+','+str(value[1])+','+str(value[2])+'\n')

newfile.close()
