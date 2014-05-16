import random
import re

def poker(hands):
	h = deal(hands)
	n = 1
	while n <= len(h):
		print "Hand", n, ":", h[n-1], "\n" 
		n = n + 1
	
	print "\nWinner hand:"
	return allmax(h, key=hand_rank)

def hand_rank(hand):
	
	ranks = card_ranks(hand)

	if straight(ranks) and flush(hand):
		return (8, max(ranks))
		

	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))

	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))

	elif flush(hand):
		return (5, max(ranks))

	elif straight(ranks):
		return (4, max(ranks))

	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)

	elif two_pair(ranks):
		return (2, two_pair(ranks), kind(1, ranks))

	elif pair(ranks):
		return (1, max(ranks), ranks)

def card_ranks(hand):
	ranks = ["--23456789TJQKA".index(r) for r, s in hand]
	ranks.sort(reverse=True)
	return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

def straight(ranks):
	return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def pair(ranks):
	return len(set(ranks)) == 4

def flush(hand):
	flushsort = [s for r, s in hand]
	return len(set(flushsort)) == 1

def kind(nr, ranks):
	for r in ranks:
		if ranks.count(r) == nr:
			return r
	return None

def two_pair(ranks):
	pair = kind(2, ranks)
	lowpair = kind(2, list(reversed(ranks)))
	if pair and lowpair != pair:
		return (pair, lowpair)
	else:
		return None

def allmax(iterable, key=None):
	iterable.sort(key=key, reverse=True)
	result = [iterable[0]]
	maxValue = key(iterable[0]) if key else iterable[0]
	for value in iterable[1:]:
        	v = key(value) if key else value
        	if v == maxValue: result.append(value)
        	else: break
	return result

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
	random.shuffle(deck)
	shuffeleddeck = [deck[n*i:n*(i+1)] for i in range(numhands)]
	return shuffeleddeck

