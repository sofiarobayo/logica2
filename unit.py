def unitPropagate(clausula, I):
    #Input: conjunto de clausulas,
    #I, interpretacion parcial
    #Output: S, conjunto de clausulas,
    #I, interpretacion parcial
	lau= clausUnit(clausula)
	while(clausvacia not in clausula and lau):
		for i in clausula:
			if len(i) == 1:
				l = i[0]
		clausula = [y for y in clausula if l not in y]
		for w in clausula:
			if compllit(l) in w:
				w.remove(compllit(l))
		if l[0] == '~':
			I[l[1]] = 0
		else:
			I[l] = 1
		lau = clausUnit(clausula)
	return clausula, I
