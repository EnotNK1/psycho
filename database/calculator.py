from typing import List

class Calculator:
    def sum_specific_elements(self, answers: List[int], indices: List[int]) -> int:
        return sum(answers[i-1] for i in indices)

    def test_maslach_calculate_results(self, answers: List[int]):
        indices_1 = [1, 2, 3, 8, 13, 14, 16, 20]
        indices_2 = [5, 10, 11, 15, 22]
        indices_3 = [4, 7, 9, 12, 17, 18, 19, 21]
        scale_1_sum = calculator_service.sum_specific_elements(answers, indices_1)
        scale_2_sum = calculator_service.sum_specific_elements(answers, indices_2)
        scale_3_sum = calculator_service.sum_specific_elements(answers, indices_3)
        return scale_1_sum, scale_2_sum, scale_3_sum

calculator_service = Calculator()