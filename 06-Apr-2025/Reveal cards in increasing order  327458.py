# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0]*len(deck)
        ind = deque(range(len(deck)))
        for card in deck:
            idx = ind.popleft()
            ans[idx] = card
            if ind:
                ind.append(ind.popleft())
        return ans

            

            
