"""--- Part Two ---
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?"""



from functools import cmp_to_key


def compare(s1: str, s2:str) -> int:
    """
        Input:  two strings that must be compared

        Output: -1 if s1 < s2, +1 if s1 > s2, 0 if they are equals

        This method overrides the usual compare method, so hands are sorted as 
        the game requires and not using the usual sort strings criteria.
    """
    def compare_by_cards_value(s1: str, s2: str) -> int:
        """
            Input:  two strings that must be compared

            Output: -1 if s1 < s2, +1 if s1 > s2, 0 if they are equals

            Substitutes every character of the strings (card) with a number 
            that represents its value, then compare the values of each card of 
            each string in order as they are.
        """
        values: dict[str, int] = {"J": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T":9, "Q":10, "K":11, "A":12}
        s1_tmp: list[int] = [ values[char] for char in s1 ]
        s2_tmp: list[int] = [ values[char] for char in s2 ]
        for i in range(0, len(s1_tmp)):
            if s1_tmp[i] > s2_tmp[i]:
                return 1
            elif s1_tmp[i] < s2_tmp[i]:
                return -1
        return 0

    def hand_value(s: str) -> int:
        """
            Input:  a string 

            Output: a value that represents how strong is the hand represented 
                    by the string: 
                        - 6 if all the cards are the same
                        - 5 if there is a four of a kind
                        - 4 if there is a full (tris + couple)
                        - 3 if there is a tris
                        - 2 if there are  two couples
                        - 1 if there's a couple
                        - 0 if none of the above
            
            Use same to count the occurrences of a single card, than use max to 
            get the max number of occurrences.

            Add the joker's mechanic so Js are added the most common cards of 
            each hand. Remove all the Js from the input and count them, finally 
            add the number of Js to most common cards.
        """
        pool_of_j: int = 0
        while s.find("J") != -1:
            pool_of_j += 1
            s = s.replace("J", "", 1)
        if pool_of_j == 5:
            return 6
        same: list[int] = [1]
        if len(s) > 1:
            for i in range(0, len(s)-1):
                if s[i] == s[i+1]:
                    same[len(same)-1] += 1
                else:
                    same.append(1)
        if max(same)+pool_of_j >= 4:
            return max(same)+pool_of_j+1
        if max(same)+pool_of_j == 3:
            same.remove(max(same))
            if max(same) == 2:
                return 4
            else:
                return 3
        if max(same)+pool_of_j == 2:
            same.remove(max(same))
            if max(same) == 2:
                return 2
            else:
                return 1
        return 0
    
    s1o: str = "".join(sorted(list(s1)))
    s2o: str = "".join(sorted(list(s2)))
    s1hv: int = hand_value(s1o)
    s2hv: int = hand_value(s2o)
    if s1hv > s2hv:
        return 1
    elif s1hv < s2hv:
        return -1
    return compare_by_cards_value(s1, s2)



def calculate(hands: dict[str, int]) -> int:
    sorted_hands = sorted(hands.keys(), key=cmp_to_key(compare))
    res = 0
    for i, h in enumerate(sorted_hands):
        res += (i+1)*hands[h]
    return res



with open('day_07/input', 'r') as f:
#with open('day_07/test_input_1', 'r') as f:
    l = f.readlines()
d: dict[str, int] = {}
for line in l:
    d[line.split()[0]] = int(line.split()[1])
print(calculate(d))
