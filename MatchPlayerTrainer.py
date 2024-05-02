class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        p = 0
        t = 0
        count = 0
        while p < len(players) and t < len(trainers):
            if players[p] > trainers[t]:
                t+=1
            else:
                count+=1
                t+=1
                p+=1
                if p >= len(players):
                    break
        return count
