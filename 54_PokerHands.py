suits = ['C','D','H','S']
cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

ranks = ['hc','op','tp','tk','st','fl','fh','fk','sf','rf']
#ranks with corresponding vals
#hc, op, tp, tk, fh, fk

def royal_flush(hand):
	suit = hand[0][1]
	target_vals = set(['T','J','Q', 'K', 'A'])
	vals = []
	for card in hand:
		if card[1] != suit:
			return False
		vals.append(card[0])
	vals = set(vals)
	if vals == target_vals: return ('rf', )
	else: return False

#print royal_flush(['TH','JH','QH','KH','AH'])

def straight_flush(hand):
	straight = None
	flush = True

	suit = hand[0][1]
	indices = []
	for card in hand:
		if card[1] != suit:
			flush = False
		indices.append(cards.index(card[0]))
	indices.sort()
	first = indices[0]
	last = indices[-1]
	if indices == range(first, last+1):
		straight = True
	else:
		straight = False
	if straight and flush:
		return ('sf', )
	elif straight:
		return ('st', )
	elif flush:
		return ('fl', )
	else:
		return False

#print straight_flush(['2H','3H','4H','6H','5H'])

'''
def four_of_a_kind(hand):
	val = hand[0][0]
	for card in hand:
		if card[0] != val:
			return False
	return 'fk',
'''

def full_house(hand):
	fh = False
	three_of_a_kind = False
	four_of_a_kind = False
	two_pairs = False
	one_pair = False

	mag = None

	vals = []
	freqs = {}
	for card in hand:
		val = card[0]
		if not(val in vals):
			vals.append(val)
			freqs[val] = 0
		freqs[val] += 1
	freq_values = freqs.values()
	freq_values.sort()
	if freq_values == [2,3]:
		fh = True
		for card, freq in freqs.items():
			if freq == 3:
					mag = card
	if 4 in freq_values:
		four_of_a_kind = True
		for card, freq in freqs.items():
			if freq == 4:
				mag = card
	if 3 in freq_values:
		three_of_a_kind = True
		for card, freq in freqs.items():
			if freq == 3:
				mag = card
	if 2 in freq_values and fh == False:
		one_pair = True
		freq_values.remove(2)
		if freq_values != None:
			if 2 in freq_values:
				two_pairs = True
				for card, freq in freqs.items():
					if freq == 2:
						if mag != None:
							if cards.index(card) > cards.index(mag):
								mag = card
						else:
							mag = card
			else:
				for card, freq in freqs.items():
					if freq == 2:
						mag = card
	if fh:
		return 'fh', mag
	if four_of_a_kind:
		return 'fk', mag
	if three_of_a_kind:
		return 'tk', mag
	if two_pairs:
		return 'tp', mag
	if one_pair:
		return 'op', mag
	else:
		return False
#print full_house(['3C','3D','3S','9S','9D'])

def high_card(hand):
	inds = []
	for card in hand:
		val = card[0]
		inds.append(cards.index(val))	
	max_ind = max(inds)
	return ('hc', cards[max_ind])

def rank_hand(hand):
	val = royal_flush(hand)
	if val == False: 
		val = straight_flush(hand)
		if val == False: 
			val = full_house(hand)
			if val == False: 
				val = high_card(hand)
	return val

def compare_hands(hand1,hand2):
	val1 = rank_hand(hand1)
	val2 = rank_hand(hand2)
	val1_ind = ranks.index(val1[0])
	val2_ind = ranks.index(val2[0])
	if val1_ind > val2_ind:
		return '1'
	elif val1_ind < val2_ind:
		return '2'
	else: 
		if len(val1) == 2:
			#print hand1
			#print val1
			val1_mag_ind = cards.index(val1[1])
			val2_mag_ind = cards.index(val2[1])
			if val1_mag_ind > val2_mag_ind:
				return '1'
			elif val2_mag_ind > val1_mag_ind:
				return '2'
			else:
				return equality_case(hand1, hand2)
		else:
			return equality_case(hand1, hand2)

def remove_val(val, hand):
	for item in suits:
		card = str(val)+item
		try: 
			hand.remove(card)
		except:
			pass
	return hand

def equality_case(hand1, hand2):
	val1_ind = []
	val2_ind = []
	for card in hand1:
		val1_ind.append(cards.index(card[0]))
	for card in hand2:
		val2_ind.append(cards.index(card[0]))
	max1 = max(val1_ind)
	max2 = max(val2_ind)

	if max1 > max2:
		return '1'
	elif max1 < max2:
		return '2'
	else:
		card1 = cards[max1]
		card2 = cards[max2]
		#hand1.remove(card1)
		#hand2.remove(card2)
		hand1 = remove_val(card1, hand1)
		hand2 = remove_val(card2, hand2)
		return equality_case(hand1, hand2)

def tests():
	h11 = ['5H','5C','6S','7S','KD']
	h12 = ['2C','3S','8S','8D','TD']
	h21 = ['5D','8C','9S','JS','AC']
	h22 = ['2C','5C','7D','8S','QH']
	h31 = ['2D','9C','AS','AH','AC']
	h32 = ['3D','6D','7D','TD','QD']
	h41 = ['4D','6S','9H','QH','QC']
	h42 = ['3D','6D','7H','QD','QS']
	h51 = ['2H','2D','4C','4D','4S']
	h52 = ['3C','3D','3S','9S','9D']

	print rank_hand(h11)
	print rank_hand(h12)
	print rank_hand(h21)
	print rank_hand(h22)
	print rank_hand(h31)
	print rank_hand(h32)
	print rank_hand(h41)
	print rank_hand(h42)
	print rank_hand(h51)
	print rank_hand(h52)

	print('=========')

	print compare_hands(h11, h12)
	print compare_hands(h21, h22)
	print compare_hands(h31, h32)
	print compare_hands(h41, h42)
	print compare_hands(h51, h52)
		
def main():
	p1_wins = 0
	p2_wins = 0
	p1_win_cards = []
	ctr = 1
	with open('54_data.txt', 'rb') as f:
		while True:
			
			line = f.readline().split()
			if line == []:
				break
			hand1 = line[:5]
			hand2 = line[5:]

			if compare_hands(hand1, hand2) == '1':
				p1_wins += 1
				p1_win_cards.append(ctr)
			elif compare_hands(hand1, hand2) == '2':
				p2_wins += 1
			else:
				pass
				#print compare_hands(hand1, hand2)
				#print (hand1, hand2)
				#print ctr
				#print "WAT"
			ctr += 1


	print p1_wins
	#print p2_wins
	#print p1_win_cards

#tests()
main()

#a = ['TH', '8H', '5C', 'QS', 'TC']

#a = ['KS','KC','9S','6D','2C']
#b = ['QH','9D','9H','TS','TC']


#print rank_hand(a)
#print full_house(b)
#print rank_hand(b)
#print compare_hands(a,b)


'''
a = ['6H','5D','7S','5H','9C'] 
b = ['9H', 'JH', '8S', 'TH','7H']
print compare_hands(a,b)

print rank_hand(a)
print rank_hand(b)
print equality_case(a,b)
'''



