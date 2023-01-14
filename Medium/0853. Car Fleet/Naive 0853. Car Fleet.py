from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_ls = [(pos, sp) for pos, sp in zip(position, speed)]
        car_ls = sorted(car_ls, key=lambda car: car[0])

        stack = [car_ls.pop()]
        while car_ls:
            curr_car = car_ls.pop()
            cc_at = (target - curr_car[0]) / curr_car[1]

            last_car = stack[-1]
            lc_at = (target - last_car[0]) / last_car[1]

            if cc_at > lc_at:
                stack.append(curr_car)

        return len(stack)
