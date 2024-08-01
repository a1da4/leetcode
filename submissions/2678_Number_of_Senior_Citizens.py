class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        def _getInfo(detail: str) -> Tuple[int, str, int, int]:
            phone = detail[:10]
            gender = detail[10]
            age = detail[11:13]
            seat = detail[13:]
            return int(phone), gender, int(age), int(seat)
        
        answer = 0
        for detail in details:
            _, _, age, _ = _getInfo(detail)
            if age > 60:
                answer += 1
    
        return answer
