from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_ls = [(pos, sp) for pos, sp in zip(position, speed)]
        car_ls = sorted(car_ls)[::-1]

        stack = []
        for p, s in car_ls:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


        print(car_ls)


if __name__ == '__main__':
    ppp = [10, 8, 0, 5, 3]
    sss = [2, 4, 1, 1, 3]
    ttt = 12
    print(Solution().carFleet(ttt, ppp, sss))
