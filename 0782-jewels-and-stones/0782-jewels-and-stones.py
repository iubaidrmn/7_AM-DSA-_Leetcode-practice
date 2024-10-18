class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # count = []
        # count = jewels.intersection(stones)
        # return len(count)
         
        # count = 0
        # # Iterate through each stone
        # for stone in stones:
        #     # If the stone is a jewel, increment the count
        #     if stone in jewels:
        #      count += 1
        # return count

        stone_count = Counter(stones)

        count = 0
        for jewel in jewels:
            count += stone_count[jewel]
        return count