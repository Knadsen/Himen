# -*- coding: latin-1 -*-

#
#  IS-105 LAB5
#
#  lab5.py - kildekode som inneholder studentenes løsning.
#         
#
#


# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Simen Knudsen', \
			'student2': 'Sondre Søbye', \
}

# Oppgave 
# 	Implementere pokerspill. Vi begynner med representasjon og testing.
#
#	Testing i Python kan gjøres med assert. Eksemplet under skal være selvforklarende.
#
#   Det er gitt et kortstokk http://en.wikipedia.org/wiki/Playing_card med 52 kort.
#	I denne oppgaven prøver vi å lage et prototype som gir svar på følgende:
#	Hvordan representere alle kort? Hvordan finne ut hvilken hånd er best?
#
#   Les deg opp på hva poker er og hvordan det spilles, hvis du ikke kjenner til det fra før.
#	Domenkunnskap i systemutvikling er viktigst!!!
#	http://no.wikipedia.org/wiki/Poker
#	http://en.wikipedia.org/wiki/Poker
#
#	Her er et forslag for representasjon av kort og hender, som jeg anbefaler dere å bruke.
#	Dere kan gjøre egne modifikasjoner, med de må være begrunnet i lab5defs.txt filen.
#
#   Typer (kind): H - heart, S - spade, C - club, D - diamond (13 kort av hver type)
#   Verdi (rank): A - ace, K - king, Q - queen, J - jack, T - ten, 9, 8, 7, 6, 5, 4, 3, 2
#   En hånd (hand): består av 5 kort http://en.wikipedia.org/wiki/Hand_rankings
#   Hånd rangeres fra høyest til lavest (i paranteser anbefalt navn på variab: 
#		 8 - Straight flush (sf) (finnes også Royal Flush, som er den beste av Straight flush
#		 7 - Four of a Kind (fk) 
#		 6 - Full House (fh) 
#	     5 - Flush (fl)
#		 4 - Straight (st) 
#		 3 - Three of a kind (tk) 
#	     2 - Two Pair (tp) 
#        1 - One Pair (op) 
#        0 - High Card (hc)
#   
#
def poker(hands):
	"""
		Returnerer den beste hånden: poker([hand, ...]) => hand
		hand_rank er en funksjon som må skrives og brukes i sammenligningen av "hender"
		Foreløpig fungerer den ikke
	"""
	return max(hands, key=hand_rank)

# Dette er et skall for en funksjon du kan skrive, men det er ikke en oppgave i denne laben.
# Du kan jobbe videre med denne funksjonen i påfølgende laber.
def hand_rank(hand):
	"""
		Returnerer en verdi som indikerer verdi av en hånd. 
		Vi har gitt verdien til hendene i spesifikasjonen (8 Straight Flush, ...)
		Vi må også kunne skille mellom "like" hender (breaking ties).
		9 9 9 9 5 => (7,9,5) Four of Kind (7) and fife kicker
		3 3 3 3 2 => (7,3,2) Four of Kind (7) and two kicker
		TD 8D 7D 5D 3D => (5, [10,8,7,5,3]) Flush (5) men alle kort må spesifiseres for å kunne sammenligne
		JC TC 9C 8C 7C => (8, 11) Straight Flush (8) Jack (11) High
		AS AH AC AD QH => (7, 14, 12) Four Aces (7, 14)  and a Queen kicker (12)
	"""
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks)) # 2 3 4 5 6 => (8, 6)
	elif kind(4, ranks): # kan returnere både boolean og tall, i Java 0 er False
		return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3 (7, 9, 3)
	#elif ...
	
# Funksjonene card_ranks(hand) returnerer en ORDNET tuple av verdier (ranks)
# Verdier for J, Q, K og A er tilsvarende 11, 12, 13, 14. 
# En hånd TD TC TH 7C 7D skal returnere [10,10,10,7,7]
def card_ranks(hand):
	score = []
	for holdingHand in hand:
		x = holdingHand[0]
		if (x == 'T'):
			score.append(10)
		elif (x == 'J'):
			score.append(11)
		elif (x == 'Q'):
			score.append(12)
		elif (x == 'K'):
			score.append(13)
		elif (x == 'A'):
			score.append(14)
		else:
			score.append(int(x))
	return score

# Disse hjelpefunksjonene skal vi jobbe med videre i senere lab oppgaver.
# Funksjonen straight(ranks) returner True hvis hånden er en Straight.
def straight(ranks):
	return None

# Funksjonen flush(hand) returnerer True hvis hånden er en Flush.
def flush(hand):
	return None

# Funksjonen kind(nr, ranks) returnerer den første verdien (rank) som hånden har nøyaktig n av.
# For en hånd med 4 syvere, skal denne funksjonen returnere 7.
def kind(nr, ranks):
	return None

# Funksjonen two_pair(ranks) gjør følgende:
# hvis det er Two Pair, skal funksjonen returnere deres verdi (rank) som en tuple.
# For eksempel, en hånd med to toere og 2 firere vil gi en returverdi på (4, 2).
def two_pair(ranks):
	return None


def test():
   
	# Oppgave 1
	# Den innebygde (built-in) funksjonen max kan brukes for å finne den beste hånden
	# Skriv test for den innebygde funksjonen max på flere "list of numbers" (lon)
	# Eksemplene er gitt, du må kommentere disse ut og sette på en verdi som ikke gir feil
	lon1 = [6, 7, 8, 0]
	lon2 = [6, 7, -9, 0]
	lon3 = [2, 5, 3, 9]
	lon4 = [3, 5, -1, 6]
	assert max(lon1) == 8
	assert max(lon2, key=abs) == -9
	assert max(lon3) == 9
	assert max(lon4) == 6


	sf = "6C 7C 8C 9C TC".split() # Straight Flush => ['6C', '7C', '8C', '9C', 'TC']
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	fl = "QC AC 4C 2C 7C".split() # Flush
	st = "5H 6C 7D 8H 9D".split() # Straight
	tk = "4D 8C 4S 4C 9D".split() # Three of a kind
	tp = "QH 8C 4D 8H QS".split() # Two pair
	op = "KD KH 6C 3D 9H".split() # One pair

	
	assert poker([sf, fk, fh, fl, st, tk, tp, op]) == sf
	# Oppgave 2 
	# Skriv tre nye testtilfeller som sammenligner hender basert på eksemplet overfor
	# 1) Four of Kind (fk) mot Full House (fh) skal returnere Four of Kind (fk)
	# 2) Full House (fh) mot Full House (fh) skal returnere Full House (fh)
	# 3) Straight (st) skal slå Two pair (tp) OBS! Du må selv lage eksempler på hender her
	
	assert poker([fk, fh]) == fk
	assert poker([fh, fh]) == fh
	assert poker([st, tp]) == st

	# Oppgave 3
	# Skriv 2 nye testtilfeller:
	# 1) teste et tilfelle der det kun er en hånd og at poker returnerer den samme hånden
	# 2) teste et tilfelle hvor man sammenligner en Straight Flush med 100 Full Houses
	# og det må da returnere Straight Flush (urealistisk med så mange spillere, men 
	# vi tar høyde for det).
	# Hva skjer hvis man har en tom liste som inn-data, dvs. ingen hender?

	assert poker([sf]) == sf

	st_vs_100 = [100]
	st_vs_100[0] = sf
	for i in range(1, 100):
		st_vs_100.append(fh)

	assert poker(st_vs_100)
	

	# Oppgave 4
	# Implementer funksjonen card_rank(hand) og legg til tester for 
	# sf, fk og fh variabler som er definert i denne testfunksjonen
	# Du kan gjerne definere flere hender og legge til flere tester :)

	assert card_ranks(sf) == [6,7,8,9,10]
	assert card_ranks(fk) == [9,9,9,9,7]
	assert card_ranks(fh) == [10,10,10,7,7]
	assert card_ranks(st) == [5,6,7,8,9]
	assert card_ranks(tp) == [12,8,4,8,12]


    # 
    # Funksjonen hard_rank er ennå ikke implementert
	# Her er gitt noen eksempler på testing av denne funksjonen som man kan bruke på et senere tidspunkt
    #
	#assert hand_rank(sf) == (8,10)
	#assert hand_rank(fk) == (7,9,7)
	#assert hand_rank(fh) == (6,10,7)
	return "Done testing"

print test()


