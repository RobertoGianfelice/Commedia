filenameInput="./Commedia.txt"
filenameOutput="./CommediaTuttoDiUnFiato.txt"
caratteriDaSaltare=["\n",",","."," ","'"]
fI=open(filenameInput,"r")
fO=open(filenameOutput, "w")
while True:
	c = fI.read(1)
	if not c:
		print ("End of file")
		break
	if c in caratteriDaSaltare:
		print("Salta")
	else:
		fO.write(c)
		print ("Read a character:", c)
fO.close()
