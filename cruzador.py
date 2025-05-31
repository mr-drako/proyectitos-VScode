#formato a usar:
#lunes: ,,o,,,,o,
#martes: ,o,,o,,,,
#etc, o es ocupado, nada es espacio libre
#basado en el horarios por bloque, de la uc
#no considera el bloque de almuerzo***

def traduc(l):
    d=["lunes","martes","miercoles","jueves","viernes"]
    h=["8:20-9:30","9:40-10:50","11:00-12:10","12:20-13:30","14:50-16:00","16:10-17:20","17:30-18:40","18:50-20:00","20:10-21:20"]
    print(d[l[0]]+",bloque",l[1]+1,h[l[1]])
    return
n=int(input("cuantos horarios? "))
nom=[]
el=[]
fd=[]
for i in range(n):
    nh=input("nombre del horario/persona ")
    nh=nh.lower()
    nh="horarios/"+nh+".txt"
    nom.append(nh)
for e in nom:
    x=open(e,"r")
    ho=x.readlines()
    for i in range(len(ho)):
        ho[i]=ho[i].strip("\n")
        ho[i]=ho[i].split(",")
    for dia in range(5):
        for hora in range(len(ho[dia])):
            if ho[dia][hora] == "":
                    el.append([dia,hora])
    x.close()
for e in el:
    if (el.count(e) == n) and (e not in fd):
         fd.append(e)
if len(fd)>0:
    print("todos estan disponibles el:")
    for e in fd:
        traduc(e)
else:
    print("no hay momento donde todos esten disponibles :(")
    print("en estas horas solo 1 persona no puede") 
    for e in el:
        if (el.count(e) == n-1) and (e not in fd):
            fd.append(e)