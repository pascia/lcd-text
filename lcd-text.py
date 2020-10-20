from matplotlib import pyplot as plt
from numpy.random import default_rng
rng = default_rng()

text = "0123 abcdef"
char = len(text)
lcdtext = []

#letter display data
#data type: 4=ON 1=OFF, 
#[TOP,TOPLEFT,TOPRIGHT,MIDDLE,BOTTOMLEFT,BOTTOMRIGHT,BOTTOM]
for letter in text:
    if letter == "0":
        lcdtext.append([7,7,7,1,7,7,7])
    if letter == "1":
        lcdtext.append([1,1,7,1,1,7,1])
    if letter == "2":
        lcdtext.append([7,1,7,7,7,1,7])
    if letter == "3":
        lcdtext.append([7,1,7,7,1,7,7])
    if letter == " ":
        lcdtext.append([1,1,1,1,1,1,1])
    if letter == "a":
        lcdtext.append([7,7,7,7,7,7,1])
    if letter == "b":
        lcdtext.append([7,7,7,7,7,7,7])
    if letter == "c":
        lcdtext.append([7,7,1,1,7,1,7])
    if letter == "d":
        lcdtext.append([7,7,7,1,7,7,7])
    if letter == "e":
        lcdtext.append([7,7,1,7,7,1,7])
    if letter == "f":
        lcdtext.append([7,7,1,7,7,1,1])      

#create a blank textured numpy screen
scrnp = rng.choice(a=[0,0.4], size=(96+15,(char*50)+30))

#render algorithm
for i in range(len(lcdtext)):
    for a in range(6):
        scrnp[15+a,28+(i*50)+a:60+(i*50)-a]=(lcdtext[i])[0]
    for a in range(6):
        scrnp[18+a:55-a,25+(i*50)+a]=(lcdtext[i])[1]
    for a in range(6):
        scrnp[18+(5-a):55-(5-a),57+(i*50)+a]=(lcdtext[i])[2]
    for a in range(7):
        if a==0 or a==1 or a==2 or a==3:
            scrnp[53+a,32+(i*50)-a:57+(i*50)+a]=(lcdtext[i])[3]
        else:
            scrnp[53+a,32+(i*50)+a-6:57+(i*50)-a+6]=(lcdtext[i])[3]
    for a in range(6):
        scrnp[58+a:35+58-a,25+(i*50)+a]=(lcdtext[i])[4]
    for a in range(6):
        scrnp[58+5-a:35+58+a-5,32+25+(i*50)+a]=(lcdtext[i])[5]
    for a in range(6):
        scrnp[75+15+a,28+5+(i*50)-a:60-5+(i*50)+a]=(lcdtext[i])[6]

#Photo desing part
fig = plt.figure()
plt.imshow(scrnp, cmap="gray", vmax=7, vmin=0)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)#clear xaxis info
ax.axes.yaxis.set_visible(False)#clear yaxis info
plt.show()
fig.savefig('./lcd_.jpg')