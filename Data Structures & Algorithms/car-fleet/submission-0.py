class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(x, y) for x, y in zip(position, speed)]
        print(pair)
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        print(prevTime)

        for i in range(1, len(pair)):
            current_car = pair[i]
            currentTime = (target - current_car[0]) / current_car[1]
            if currentTime > prevTime:
                fleets+= 1
                prevTime = currentTime

        return fleets