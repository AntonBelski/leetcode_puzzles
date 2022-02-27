class Solution:
    def totalFruit(self, fruits):
        fruits_dict = {}
        start_ind = 0
        counter = 0
        max_counter = 0
        for elem in fruits:
            counter += 1
            if fruits_dict.get(elem):
                fruits_dict[elem] += 1
            else:
                fruits_dict[elem] = 1

            while len(fruits_dict) > 2:
                fruits_dict[fruits[start_ind]] -= 1
                if not fruits_dict[fruits[start_ind]]:
                    fruits_dict.pop(fruits[start_ind])
                counter -= 1
                start_ind += 1

            max_counter = max(max_counter, counter)
        return max_counter


if __name__ == '__main__':
    solution = Solution()
    my_nums = [0, 1, 2, 2]
    res = solution.totalFruit(my_nums)
    print(res)
