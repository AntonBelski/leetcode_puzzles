from collections import Counter
from typing import List


class Solution:
    def asteroidsDestroyed2(self, mass: int, asteroids: List[int]) -> bool:
        sorted_asts = sorted(asteroids)
        planet_mass = mass

        for ast_mass in sorted_asts:
            if ast_mass > planet_mass:
                return False
            planet_mass += ast_mass

        return True

    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids_freq = Counter(asteroids)
        planet_mass = mass

        for mass in range(1, 100001):
            if asteroids_freq[mass]:
                if mass > planet_mass:
                    return False
                else:
                    planet_mass += mass * asteroids_freq[mass]

        return True


if __name__ == '__main__':
    solution = Solution()
    mass = 10
    asteroids = [3, 9, 19, 5, 21]
    result = solution.asteroidsDestroyed(mass, asteroids)
    print(result)
    result = solution.asteroidsDestroyed(mass, asteroids)
    print(result)
