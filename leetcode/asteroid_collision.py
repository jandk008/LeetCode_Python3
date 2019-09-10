class Solution(object):
    def asteroid_collision(self, asteroids):
        if len(asteroids) < 2:
            return asteroids
        res = []
        for asteroid in asteroids:
            while res and asteroid < 0 < res[-1]:
                if res[-1] < -asteroid:
                    res.pop()
                    continue
                elif res[-1] == -asteroid:
                    res.pop()
                break
            else:
                res.append(asteroid)
        return res
