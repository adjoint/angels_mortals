# -*- coding: utf-8 -*-
import csv
import copy 
with open('responses.csv', 'rb') as f:
    reader = csv.reader(f)
    angels = map(list, reader)
# print l
del angels[0]  
mortals = copy.deepcopy(angels)
print mortals



matches = []
matched = []
matcheslong = []
matchedlong = []
def match(a,b):
    matcheslong.append([angels[a][1], angels[a][4], angels[a][2], mortals[b][1], mortals[b][2], mortals[b][5], mortals[b][6], mortals[b][7], mortals[b][12]])
    matchedlong.append([mortals[b][1], mortals[b][4], mortals[b][2], angels[a][3], angels[a][13]])
    matches.append((angels[a][1], mortals[b][1]))
    matched.append((mortals[b][1], angels[a][1], angels[a][3]))
    angels[a][0] = 0
    mortals[b][0] = 0

file = open("people_colleges.csv", "w")
for a in range(len(angels)):
    file.write(angels[a][1] + ', ' + angels[a][6] + '\n')
file.close()

file = open("another.txt", "w")
add = []
for a in range(len(angels)):
    if angels[a][6] == "I don't mind another mortal":

        file.write(angels[a][1] + ' <' + angels[a][4] + '>\n')
        add.append ( (angels[a][1]) )
print add
file.close()

for a in range(len(angels)):
    for b in range(len(mortals)):
        if angels[a][0] != 0 and mortals[b][0] != 0 and a != b and angels[a][8] != '':
            if mortals[b][1] == angels[a][8]:
                match(a,b)
                break
               
for a in range(len(angels)):
    for b in range(len(mortals)):  
        if a != b and angels[a][0] != 0 and mortals[b][0] != 0:
            if ((mortals[b][1], angels[a][1]) in matches):
                continue          
            if angels[a][9] == 'Yes':
                if angels[a][10] == 'Yes':
                    if angels[a][5] == mortals[b][5] and angels[a][6] == mortals[b][6]:
                        match(a,b)
                        break
                elif angels[a][6] == angels[b][6]:
                    match(a,b)
                    break
            elif angels[a][10] == 'Yes':
                if mortals[a][5] == mortals[b][5]:
                    match(a,b)
                    break
            else:
                match(a, b)
                break

if angels[len(angels)-1][0] != 0:
    for b in range(len(mortals)):
        if mortals[b][0] != 0 and a!=b:
            if ((mortals[b][1], angels[a][1]) in matches):
                continue
            match(len(angels)-1, b)
            break
                
if mortals[len(mortals)-1][0] != 0:
    for b in range(len(angels)):
        if angels[b][0] != 0 and a!=b:
            if ((angels[len(mortals)-1][1], mortals[b][1]) in matches):
                continue
            match(b, len(mortals)-1)
            break                     

    

file = open("matches.csv", "w") 
file.write("Angel, Mortal\n")
for m in matches:
    file.write(m[0] + ', ' + m[1] +'\n')
file.close()
       
print matches
print 'OK'
print matched

if len(matches) == len(angels):
    print 'can'
else:
    print len(matches), len(angels)
            
#for a in range(len(angels)):
#    print angels[a][0], angels[a][1]    
    
#for a in range(len(mortals)):
#    print mortals[a][0], mortals[a][1] 

send = []
for a in matcheslong:
    for b in matchedlong:
        if a[1] == b[1]:
            send.append([a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], b[3], b[4]])
            

file = open("tosend.txt", "w")
for a in send:
    string8 = ''
    string9 = ''
    string10 = ''
    if a[8] != '':
        string8 = 'They passed the following information to you: ' + a[8] + '\n\n'
    if a[9] != '':
        string9 = '\nThey would like to go by ' + a[9] + '.'
    if a[10] != '':
        string10 = '\nThey would also like you to know this: ' + a[10]
    string = "{0} <{1}>\n\nAngels and Mortals 2016\n\nDear {2},\n\nThanks again for signing up for \"Angels and Mortals\"!\nOur matching program worked its magic and your mortal is:\n\n{3}\nPrefers to be called: {4}\nClass: {5}\nRC: {6}\
    \nRoom: {7}\n\n".format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
    string1 = string + string8 + "As part of the game you also get your own Angel! They should contact you soon." + string9 +  string10 + "\n\nMeanwhile, please join this group for ideas and keeping in touch: [link to facebook group]"+ "\n\nIf you have any questions, please direct them to this e-mail.\n\nHappy Blessing!\n\nAll my best,\n[name of organizer]"  
    
    tosend='\n\n\n' + string1
    file.write(tosend)
file.close()
for a in angels:
    if a[0] != 0:
        print a[1]
for a in mortals:
    if a[0] != 0:
        print a[1]