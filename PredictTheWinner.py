class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def score(nums, player1, player2, turn):
            if len(nums) == 1:
                if turn % 2 == 0:
                    player1 += nums[0]
                else:
                    player2 += nums[0]
                return player1 >= player2
            if turn % 2 == 0:
                new_player1 = player1 + nums[0]
                new_player2 = player2
            else:
                new_player1 = player1
                new_player2 = player2 + nums[0]

            pick_first = score(nums[1:], new_player1, new_player2, turn + 1)

            if turn % 2 == 0:
                new_player1 = player1 + nums[-1]
                new_player2 = player2
            else:
                new_player1 = player1
                new_player2 = player2 + nums[-1]

            pick_last = score(nums[:-1], new_player1, new_player2, turn + 1)

            if turn % 2 == 0:
                return pick_first or pick_last
            else:
                return pick_first and pick_last

        return score(nums, 0, 0, 0)
