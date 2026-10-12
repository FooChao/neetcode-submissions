class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = deque()
        for asteroid in asteroids:
            if not stk:
                stk.append(asteroid)
            elif asteroid * stk[-1] > 0 or stk[-1] < 0: # same direction or last moving left
                stk.append(asteroid)
            else: # diff direction
                while stk and stk[-1] >= 0:
                    nextCollide = stk.pop()
                    if nextCollide == -asteroid: 
                        # both explode
                        break 
                    if abs(nextCollide) >= abs(asteroid):
                        stk.append(nextCollide)
                        # asteroid explode
                        break
                    else:
                        # if everything else broke keep asteroid else continue colliding
                        if not stk or stk[-1] < 0:
                            stk.append(asteroid)

        return[a for a in stk]
                        



        