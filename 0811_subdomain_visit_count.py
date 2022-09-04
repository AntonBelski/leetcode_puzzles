from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_count = defaultdict(int)

        for cpdomain in cpdomains:
            count, full_domain = cpdomain.split()

            domain_parts = full_domain.split('.')
            for start in range(len(domain_parts)):
                domain = '.'.join(domain_parts[start:])
                domains_count[domain] += int(count)

        return [str(freq) + ' ' + dom for dom, freq in domains_count.items()]


if __name__ == '__main__':
    solution = Solution()
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    result = solution.subdomainVisits(cpdomains)
    print(result)
