class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)

        for domain in cpdomains:
            count,domain = domain.split()
            count = int(count)
            fragments = domain.split(".")

            for i in range(len(fragments)):
                counts['.'.join(fragments[i:])] += count
        print(counts)
        ans = []
        for domain,count in counts.items():
            ans.append(str(count) + " " + domain)
        return ans