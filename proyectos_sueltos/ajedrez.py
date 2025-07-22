def imp_tab(t):
  n=t.dim
  f=" · "
  print("     A · B · C · D · E · F · G · H")
  for e in t.tablero:
    for i in e:
      f=f+str(i)+" · "
    print("")
    print(f"{n} {f}")
    n=n-1
    f=" · "
class Pieza:
  def __init__(self,f,c):
    self.fila=int(f)
    self.columa=int(c)
    self.tipo=""
    self.color=""
    self.posmov=[]

  def movs(self):
    self.posmov=[]
    if self.tipo=="peon":
      if self.color=="blanco":
        self.posmov.append([self.fila-1,self.columa])
        if self.fila==1:
          self.posmov.append([self.fila-2,self.columa])
      else:
        self.posmov.append([self.fila+1,self.columa])
        if self.fila==6:
          self.posmov.append([self.fila+2,self.columa])
    elif self.tipo=="torre" or self.tipo=="reina":
      for i in range(8):
        self.posmov.append([self.fila,i])
        self.posmov.append([i,self.columa])
    elif self.tipo=="caballo":
      for i in range(2):
        for j in range(2):
            for k in range(2):
                self.posmov.append([self.fila+(2-i)*((-1)**j),self.columna+(i+1)*((-1)**k)])
    elif self.tipo=="alfil" or self.tipo=="reina":
      for i in range(8):
        self.posmov.append([self.fila+i,self.columa+i])
        self.posmov.append([self.fila+i,self.columa-i])
        self.posmov.append([self.fila-i,self.columa+i])
        self.posmov.append([self.fila-i,self.columa-i])
    elif self.tipo=="rey":
      for i in range(3):
        for j in range(3):
          self.posmov.append([self.fila+1-i,self.columa+j])
    while [self.fila,self.columa] in self.posmov:
      self.posmov.remove([self.fila,self.columa])
    return self.posmov

  def __str__(self):
    t=self.tipo
    c=self.color
    x="-"
    if c=="negro":
      if t=="rey":
        x="♚"
      elif t=="reina":
        x="♛"
      elif t=="torre":
        x="♜"
      elif t=="alfil":
        x="♝"
      elif t=="caballo":
        x="♞"
      elif t=="peon":
        x="♟"
    elif c=="blanco":
      if t=="rey":
        x="♔"
      elif t=="reina":
        x="♕"
      elif t=="torre":
        x="♖"
      elif t=="alfil":
        x="♗"
      elif t=="caballo":
        x="♘"
      elif t=="peon":
        x="♙"
    return x
class Tablero:
  def __init__(self):
    self.tablero=[]
    self.dim=8
  def gen(self):
    d=self.dim
    for i in range(d):
      fila=[]
      for j in range(d):
        fila.append(Pieza(i,j))
      self.tablero.append(fila)
class juego:
  def __init__(self,t):
    self.tablero=t
    self.juega="blanco"
  def setgame(self):
    for j in range(4):
      if j==0 or j==1:
        c="negro"
        f=j
      elif j==2 or j==3:
          c="blanco"
          f=j+4
      for i in range(8):
        #peones
        if f==1 or f==6:
          self.tablero[f][i].tipo="peon"
          self.tablero[f][i].color=c
        else:
          #torres
          if i==0 or i==7:
            self.tablero[f][i].tipo="torre"
            self.tablero[f][i].color=c
          #caballos
          elif i==1 or i==6:
            self.tablero[f][i].tipo="caballo"
            self.tablero[f][i].color=c
          #alfiles
          elif i==2 or i==5:
            self.tablero[f][i].tipo="alfil"
            self.tablero[f][i].color=c
          #reina
          elif i==3:
            self.tablero[f][i].tipo="reina"
            self.tablero[f][i].color=c
          #rey
          else:
            self.tablero[f][i].tipo="rey"
            self.tablero[f][i].color=c
  def mover(self,li,lf):
    li=li.upper()
    lf=lf.upper()
    le="ABCDEFGH"
    if li[0] in le:
      fi=abs(int(li[1])-8)
      ci=le.index(li[0])
    else:
      fi=abs(int(li[0])-8)
      ci=le.index(li[1])
    if lf[0] in le:
      ff=abs(int(lf[1])-8)
      cf=le.index(lf[0])
    else:
      ff=abs(int(lf[0])-8)
      cf=le.index(lf[1])
    if self.tablero[fi][ci].color!=self.juega:
      print("No puedes mover esa pieza")
    if self.tablero[ff][cf].color==self.juega:
      print("movimiento invalido")
    if self.tablero[fi][ci].tipo=="peon":
      if abs(fi-ff)==1 and abs(ci-cf)==1:
        if self.tablero[ff][cf].color!=self.juega:
          self.tablero[fi][ci].movs().append([ff,cf])
    if [ff,cf] in self.tablero[fi][ci].movs():
      self.tablero[ff][cf]=self.tablero[fi][ci]
      self.tablero[fi][ci]=Pieza(fi,ci)
    else:
      print("Movimiento invalido")
      print("turno perdido")
  def reyes(self):
    c=False
    for e in self.tablero:
      for l in e:
        if l.tipo=="rey" and l.color==self.juega:
          c=True
    return c
  def nextturn(self):
    if self.juega=="blanco":
      self.juega="negro"
    else:
      self.juega="blanco"

#juego
t=Tablero()
t.gen()
j=juego(t.tablero)
j.setgame()
imp_tab(t)
while j.reyes():
  j.mover(input("Desde: "),input("Hasta: "))
  j.nextturn()
  imp_tab(t)
  if j.reyes()==False:
    print(f"{j.juega} perdio")