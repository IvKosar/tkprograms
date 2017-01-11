# counter_for_mum1.pyw

from tkinter import *
#from raisers import *
import database_reader
import database_writer

# create window
root = Tk()
root.title('Звітність')
root.geometry('950x340')

# initialize list of options qunatities and last changed options
a = database_reader.value_list()
last_changed = []

# initialize variables for options quantity
savevar = StringVar()
tzdovvar, elsedovvar, maynodovvar, copyvar, pidvar = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
elsezapvar, spadspravyvar, k_pkvartibudvar, minakvibudvar = StringVar(), StringVar(), StringVar(), StringVar()
darkvibudvar, elsedohvidnermaynavar, k_pzemdilvar, minyzdvar = StringVar(), StringVar(), StringVar(), StringVar()
darzdvar, ipotzdvar, ipotkvibudvar, poztzvar = StringVar(), StringVar(), StringVar(), StringVar()
dovutrymvar, pozhertvavar, spadzakonvar, spadzapovitvar = StringVar(), StringVar(), StringVar(), StringVar()
chastvpodrvar, zaboronyvar, znzaborvar, perekladvar = StringVar(), StringVar(), StringVar(), StringVar()
elsedohvar = StringVar()

# set variables to given quantity
option_variables = [tzdovvar,elsedovvar,maynodovvar,copyvar,pidvar, elsezapvar, spadspravyvar, k_pkvartibudvar,
                    minakvibudvar, darkvibudvar, elsedohvidnermaynavar, k_pzemdilvar, minyzdvar, darzdvar, 
                    ipotzdvar, ipotkvibudvar, poztzvar, dovutrymvar, pozhertvavar, spadzakonvar, spadzapovitvar,
                    chastvpodrvar, zaboronyvar, znzaborvar, perekladvar, elsedohvar]

for i in range(len(option_variables)):
    option_variables[i].set(a[i])

# functions for buttons commands
def cancel():
    if last_changed:
        a[last_changed[-1]] -= 1 
        option_variables[last_changed[-1]].set(a[last_changed[-1]])
        last_changed.pop()
        savevar.set('')
        print(a)
        
def save():
    database_writer.writer(a)
    savevar.set('Збережено!')
    
def raise_tzdov():
    a[0] += 1
    last_changed.append(0)
    tzdovvar.set(a[0])
    savevar.set('')
    
    print(a)
    
def raise_elsedov():
    a[1] += 1
    last_changed.append(1)
    elsedovvar.set(a[1])
    savevar.set('')
    print(a)
    
def raise_maynodov():
    a[2] += 1
    last_changed.append(2)
    maynodovvar.set(a[2])
    savevar.set('')
    print(a)
    
def raise_copies():
    a[3] += 1
    last_changed.append(3)
    copyvar.set(a[3])
    print(a)
    savevar.set('')

def raise_pidpys():
    a[4] += 1
    last_changed.append(4)
    pidvar.set(str(a[4]))
    savevar.set('')
    print(a)
    
def raise_elsezap():
    a[5] += 1
    last_changed.append(5)
    elsezapvar.set(str(a[5]))
    savevar.set('')
    print(a)
    
def raise_spadspravy():
    a[6] += 1
    last_changed.append(6)
    spadspravyvar.set(str(a[6]))
    savevar.set('')
    print(a)
    
def raise_k_pkavartibud():
    a[7] += 1
    last_changed.append(7)
    k_pkvartibudvar.set(str(a[7]))
    savevar.set('')
    print(a)
    
def raise_minakvibud():
    a[8] += 1
    last_changed.append(8)
    minakvibudvar.set(str(a[8]))
    savevar.set('')
    print(a)
    
def raise_darkvibud():
    a[9] += 1
    last_changed.append(9)
    darkvibudvar.set(str(a[9]))
    savevar.set('')
    print(a)
    
def raise_elsedohvidnermayna():
    a[10] += 1
    last_changed.append(10)
    elsedohvidnermaynavar.set(str(a[10]))
    savevar.set('')
    print(a)
    
def raise_k_pzemdil():
    a[11] += 1
    last_changed.append(11)
    k_pzemdilvar.set(str(a[11]))
    savevar.set('')
    print(a) 
    
def raise_minyzd():
    a[12] += 1
    last_changed.append(12)
    minyzdvar.set(str(a[12]))
    savevar.set('')
    print(a) 
    
def raise_darzd():
    a[13] += 1
    last_changed.append(13)
    darzdvar.set(str(a[13]))
    savevar.set('')
    print(a) 
    
def raise_ipotzd():
    a[14] += 1
    last_changed.append(14)
    ipotzdvar.set(str(a[14]))
    savevar.set('')
    print(a) 
    
def raise_ipotkvibud():
    a[15] += 1
    last_changed.append(15)
    ipotkvibudvar.set(str(a[15]))
    savevar.set('')
    print(a) 
    
def raise_poztz():
    a[16] += 1
    last_changed.append(16)
    poztzvar.set(str(a[16]))
    savevar.set('')
    print(a) 
    
def raise_dovutrym():
    a[17] += 1
    last_changed.append(17)
    dovutrymvar.set(str(a[17]))
    savevar.set('')
    print(a) 
    
def raise_pozhertva():
    a[18] += 1
    last_changed.append(18)
    pozhertvavar.set(str(a[18]))
    savevar.set('')
    print(a)
    
def raise_spadzakon():
    a[19] += 1
    last_changed.append(19)
    spadzakonvar.set(str(a[19]))
    savevar.set('')
    print(a)
    
def raise_spadzapovit():
    a[20] += 1
    last_changed.append(20)
    spadzapovitvar.set(str(a[20]))
    savevar.set('')
    print(a)
    
def raise_chastvpodr():
    a[21] += 1
    last_changed.append(21)
    chastvpodrvar.set(str(a[21]))
    savevar.set('')
    print(a)
    
def raise_zaborony():
    a[22] += 1
    last_changed.append(22)
    zaboronyvar.set(str(a[22]))
    savevar.set('')
    print(a)
    
def raise_znzaborony():
    a[23] += 1
    last_changed.append(23)
    znzaborvar.set(str(a[23]))
    savevar.set('')
    print(a)
    
def raise_pereklad():
    a[24] += 1
    last_changed.append(24)
    perekladvar.set(str(a[24]))
    savevar.set('')
    print(a)
    
def raise_elsedoh():
    a[25] += 1
    last_changed.append(25)
    elsedohvar.set(str(a[25]))
    savevar.set('')
    print(a)

# BUTTONS

# Cancel button
Cancelbut = Button(root, text = 'Відмінити',font = 'ARIAL 11', command = cancel)
Cancelbut.place(x = 0, y = 0)

# Save button
Savebut = Button(root, text = 'Зберегти',font = 'ARIAL 11', command = save)
Savebut.place(x = 80, y = 0)
Savelabel = Label(root, font = 'ARIAL 11', textvariable = savevar)
Savelabel.place(x = 170, y = 3)
   
# TZDoviren button
TZDovirenbut = Button(root, text = '\nДовіреніості на ТЗ', font = 'ARIAL 12', command = raise_tzdov)
TZDovirenbut.place(x = 0, y = 30)
TZDovirenlab = Label(root,width = 20,textvariable = tzdovvar, bg = 'crimson')
TZDovirenlab.place(x = 0,y = 31)

# Inshi_dovirenosti button
Elsedovbut = Button(root, text = '\nДовіреності Інші', font = 'ARIAL 12', command = raise_elsedov)
Elsedovbut.place(x = 148, y = 30)
Elsedovlab = Label(root,width = 18,textvariable = elsedovvar, bg = 'red')
Elsedovlab.place(x = 148,y = 31)

# Dovirenosti_na_mayno button
Maynodovbut = Button(root, text = '\nДовіреності на майно', font = 'ARIAL 12', command = raise_maynodov)
Maynodovbut.place(x = 278, y = 30)
Maynodovlab = Label(root,width = 24,textvariable = maynodovvar, bg = 'firebrick')
Maynodovlab.place(x = 278,y = 31)

#Kopiya button
Copybut = Button(root, text = '\nФотокопія', font = 'ARIAL 12', width = 9, command = raise_copies)
Copybut.place(x = 448, y = 30)
Copylab = Label(root,width = 12,textvariable = copyvar, bg = 'magenta')
Copylab.place(x = 448,y = 31)

# Pidpys button
Pidbut = Button(root, text = '\nПідпис', font = 'ARIAL 12',width = 6, command = raise_pidpys)
Pidbut.place(x = 538, y = 30)
Pidlab = Label(root,width = 8,textvariable = pidvar, bg = 'darkviolet')
Pidlab.place(x = 538,y = 31)

# Inshi_zapovity button
Elsezapbut = Button(root, text = '\nЗаповіти Інші', font = 'ARIAL 12', command = raise_elsezap)
Elsezapbut.place(x = 602, y = 30)
Elsezaplab = Label(root,width = 14,textvariable = elsezapvar, bg = 'darkgray')
Elsezaplab.place(x = 602,y = 31)

# Spadkovi_spravy button
Spadspavybut = Button(root, text = '\nСпадкові справи', font = 'ARIAL 12', command = raise_spadspravy)
Spadspavybut.place(x = 0, y = 79)
Spadspavylab = Label(root,width = 19,textvariable = spadspravyvar, bg = 'dimgray')
Spadspavylab.place(x = 0,y = 80)

# Dohovory k-p kvartyr & budynkiv button
K_Pkvartibudbut = Button(root, text = '\nДоговори К-П кв. і буд.', font = 'ARIAL 12', command = raise_k_pkavartibud)
K_Pkvartibudbut.place(x = 135, y = 79)
K_Pkvartibudlab = Label(root,width = 25,textvariable = k_pkvartibudvar, bg = 'greenyellow')
K_Pkvartibudlab.place(x = 135,y = 80)

# Dohovory miny kvartyr & budynkiv button
Minakvibudbut = Button(root, text = '\nДоговори міни кв. і буд.', font = 'ARIAL 12', command = raise_minakvibud)
Minakvibudbut.place(x = 312, y = 79)
Minakvibudlab = Label(root,width = 25,textvariable = minakvibudvar, bg = 'lime')
Minakvibudlab.place(x = 312,y = 80)

# Dohovory daruvania kvartyr & budynkiv button
Darkvibudbut = Button(root, text = '\nДоговори дарування кв. і буд.', font = 'ARIAL 12', command = raise_darkvibud)
Darkvibudbut.place(x = 495, y = 79)
Darkvibudlab = Label(root,width = 32,textvariable = darkvibudvar, bg = 'limegreen')
Darkvibudlab.place(x = 495,y = 80)

# Inshi dohovory vidchuzhenya neruhomoho mayna button
Elsedohvidnermaynabut = Button(root, text = '\nДоговори Інші відч. н/x майна', font = 'ARIAL 12', command = raise_elsedohvidnermayna)
Elsedohvidnermaynabut.place(x = 0, y = 128)
Elsedohvidnermaynalab = Label(root,width = 31,textvariable = elsedohvidnermaynavar, bg = 'springgreen')
Elsedohvidnermaynalab.place(x = 0,y = 129)

# Dohovory k-p zemel. dilianky button
K_Pzemdilbut = Button(root, text = '\nДоговори К-П З/Д', width = 16, font = 'ARIAL 12', command = raise_k_pzemdil)
K_Pzemdilbut.place(x = 223, y = 128)
K_Pzemdillab = Label(root,width = 21,textvariable = k_pzemdilvar, bg = 'forestgreen')
K_Pzemdillab.place(x = 223,y = 129)

# Dohovory miny z/d button
Minyzemdilbut = Button(root, text = '\nДоговори міни З/Д', width = 16, font = 'ARIAL 12', command = raise_minyzd)
Minyzemdilbut.place(x = 376, y = 128)
Minyzemdillab = Label(root,width = 21,textvariable = minyzdvar, bg = 'green')
Minyzemdillab.place(x = 376,y = 129)

# Dohovory daryvania z/d button
Darzdbut = Button(root, text = '\nДоговори дарування З/Д', width = 22, font = 'ARIAL 12', command = raise_darzd)
Darzdbut.place(x = 529, y = 128)
Darzdlab = Label(root,width = 29,textvariable = darzdvar, bg = 'darkgreen')
Darzdlab.place(x = 529,y = 129)

# Dohovory ipoteky z/d button
Ipotzdbut = Button(root, text = '\nДоговори іпотеки З/Д', font = 'ARIAL 12', command = raise_ipotzd)
Ipotzdbut.place(x = 0, y = 177)
Ipotzdlab = Label(root,width = 23,textvariable = ipotzdvar, bg = 'yellowgreen')
Ipotzdlab.place(x = 0,y = 178)

# Dohovory ipoteky kvartyr & budynkiv button
Ipotkvibudbut = Button(root, text = '\nДоговори іпотеки кв. і буд.', font = 'ARIAL 12', command = raise_ipotkvibud)
Ipotkvibudbut.place(x = 168, y = 177)
Ipotkvibudlab = Label(root,width = 29,textvariable = ipotkvibudvar, bg = 'olivedrab')
Ipotkvibudlab.place(x = 168,y = 178)

# Dohovory pozychky tz button
Dovutrymbut = Button(root, text = '\nДоговори позички ТЗ', font = 'ARIAL 12', command = raise_poztz)
Dovutrymbut.place(x = 372, y = 177)
Dovutrymlab = Label(root,width = 23,textvariable = poztzvar, bg = 'mediumspringgreen')
Dovutrymlab.place(x = 372,y = 178)

# Dohovory dovichnoho utrymania button
Dovutrymbut = Button(root, text = '\nДоговори довічного утримання', font = 'ARIAL 12', command = raise_dovutrym)
Dovutrymbut.place(x = 537, y = 177)
Dovutrymlab = Label(root,width = 33,textvariable = dovutrymvar, bg = 'mediumseagreen')
Dovutrymlab.place(x = 537, y = 178)

# Dohovory pozhertvy button
Pozhertvabut = Button(root, text = '\nДоговори пожертви', font = 'ARIAL 12', command = raise_pozhertva)
Pozhertvabut.place(x = 0, y = 226)
Pozhertvalab = Label(root,width = 22,textvariable = pozhertvavar, bg = 'darkolivegreen')
Pozhertvalab.place(x = 0,y = 227)

# Spadschyna za zakonom button
Spadzakonbut = Button(root, text = '\nСпадщина за законом', font = 'ARIAL 12', command = raise_spadzakon)
Spadzakonbut.place(x = 156, y = 226)
Spadzakonlab = Label(root,width = 24,textvariable = spadzakonvar, bg = 'gainsboro')
Spadzakonlab.place(x = 156,y = 227)

# Spadschyna za zapovitom button
Spadzapovitbut = Button(root, text = '\nСпадщина за заповітом', font = 'ARIAL 12', command = raise_spadzapovit)
Spadzapovitbut.place(x = 327, y = 226)
Spadzapovitlab = Label(root,width = 26,textvariable = spadzapovitvar, bg = 'silver')
Spadzapovitlab.place(x = 327,y = 227)

# Chastka v spil'nomy mayni podryzhia button
Chastvpodrbut = Button(root, text = '\nСвідоцтва про частку в сп. майні подружжя', font = 'ARIAL 12', command = raise_chastvpodr)
Chastvpodrbut.place(x = 511, y = 226)
Chastvpodrlab = Label(root,width = 46,textvariable = chastvpodrvar, bg = 'orangered')
Chastvpodrlab.place(x = 511,y = 227)

# Zaborony nakladeni na vidchuzhenya button
Zaboronybut = Button(root, text = '\nЗаборони Накладені на відчуження н/x майна та т/з', font = 'ARIAL 12', command = raise_zaborony)
Zaboronybut.place(x = 0, y = 275)
Zaboronylab = Label(root,width = 54,textvariable = zaboronyvar, bg = 'goldenrod')
Zaboronylab.place(x = 0,y = 276)

# Zaborony znyati na vidchuzhenya button
ZnZaboronybut = Button(root, text = '\nЗаборони Зняті на відчуження н/x майна та т/з', font = 'ARIAL 12', command = raise_znzaborony)
ZnZaboronybut.place(x = 382, y = 275)
ZnZaboronylab = Label(root,width = 49,textvariable = znzaborvar, bg = 'yellow')
ZnZaboronylab.place(x = 382,y = 276)

# Pereklady button
Perekladbut = Button(root, text = '\nПереклади', font = 'ARIAL 12', command = raise_pereklad)
Perekladbut.place(x = 728, y = 275)
Perekladlab = Label(root,width = 13,textvariable = perekladvar, bg = 'rosybrown')
Perekladlab.place(x = 728,y = 276)

# Inshi dohovory
Perekladbut = Button(root, text = '\nДоговори Інші', font = 'ARIAL 12', command = raise_elsedoh)
Perekladbut.place(x = 820, y = 275)
Perekladlab = Label(root,width = 15,textvariable = elsedohvar, bg = 'lawngreen')
Perekladlab.place(x = 820,y = 276)

mainloop()

# save results to database
save()