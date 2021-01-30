#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	puissance = (voltage * voltage)/resistance
	return puissance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	#v1[0] # Pour accéder au X
	#v1[1] # Pour accéder au Y
	if v1==[] or v2==[]:
		return True
	octo = v1[0]*v2[0] + v1[1]*v2[1]
	if octo == 0:
		return True
	else:
		return False


def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme =0
	compteur = 0
	for v in values:
		if(v >= 0):
			somme = somme + v
			compteur = compteur + 1
	avg = somme / compteur

	return avg
	# La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.

	twenties = 0
	tens = 0
	fives = 0
	ones = 0
	while value != 0:
		if value >= 20:
			twenties = value // 20
			value = value - (twenties * 20)
		elif value >= 10:
			tens = value // 10
			value = value - (tens * 10)
		elif value >= 5:
			fives = value // 5
			value = value - (fives * 5)
		elif value >= 1:
			ones = value // 1
			value = value - (ones * 1)


	return (twenties, tens, fives, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
