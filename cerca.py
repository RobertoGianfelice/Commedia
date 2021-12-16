filenameInput="./CommediaTuttoDiUnFiato.txt"
fI=open(filenameInput,"r")
paradiso=""

while True:
	linea = fI.readline(10).upper()
	if len(linea)==0:
		break
	paradiso+=linea

print(f"La linea letta è lunga {len(paradiso)} caratteri")
parola=""
while parola!="FINE":
	parola=input("Inserisci la parola da cercare: ").upper()

	if parola != "FINE" :
		if parola in paradiso:
			print(f"La parola {parola} esiste. Si ripete {paradiso.count(parola)} volte. La prima occorrenza è alla posizione {paradiso.index(parola)}")
			indice=0
			occorrenza=1
			while paradiso.find(parola,indice) != -1:
				indice=paradiso.index(parola,indice)+1
				print(f"Occorrenza {occorrenza} in posizione {indice}")
				occorrenza+=1
			
		else:
			print("La parola non esiste")

