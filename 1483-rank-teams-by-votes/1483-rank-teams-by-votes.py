class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dic = {}
        num_vote = len(votes[0])
        for v in votes:
            for i, c in enumerate(v):
                if c not in dic:
                    dic[c] = [len(votes)] * num_vote
                dic[c][i] -=1
        votes = sorted(dic.keys())
        print(votes)
        return "".join(sorted(votes, key = lambda x: dic[x]))