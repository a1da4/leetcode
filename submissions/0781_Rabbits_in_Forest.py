class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer = 0
        for num, freq in Counter(answers).items():
            num_w_me = num + 1
            answer += freq // num_w_me * num_w_me
            answer += num_w_me if freq % num_w_me > 0 else 0

        return answer

