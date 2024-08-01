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

    def test_jas_calculate_results(self, answers: List[int]):
        indices_1 = [1, 2, 3, 4, 5]
        indices_2 = [6, 7, 8, 9, 10]
        scale_1_sum = calculator_service.sum_specific_elements(answers, indices_1)
        scale_2_sum = calculator_service.sum_specific_elements(answers, indices_2)
        return scale_1_sum, scale_2_sum

    def test_dass21_calculate_results(self, answers: List[int]):
        indices_1 = [2, 4, 7, 9, 15, 19, 20]
        indices_2 = [3, 5, 10, 13, 16, 17, 21]
        indices_3 = [1, 6, 8, 11, 12, 14, 18]
        scale_1_sum = calculator_service.sum_specific_elements(answers, indices_1)
        scale_2_sum = calculator_service.sum_specific_elements(answers, indices_2)
        scale_3_sum = calculator_service.sum_specific_elements(answers, indices_3)
        return scale_1_sum, scale_2_sum, scale_3_sum

    def test_stai_calculate_results(self, answers: List[int]):
        indices_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        indices_2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
        scale_1_sum = calculator_service.sum_specific_elements(answers, indices_1)
        scale_2_sum = calculator_service.sum_specific_elements(answers, indices_2)
        return scale_1_sum, scale_2_sum

    def test_cmq_calculate_results(self, answers: List[int]):
        indices_1 = [20, 16, 15, 19, 13]
        indices_2 = [14, 8, 17, 6, 9]
        indices_3 = [43, 44, 42, 45, 23]
        indices_4 = [11, 12, 39, 40, 21]
        indices_5 = [3, 1, 2, 10, 25]
        indices_6 = [26, 38, 4, 5, 36, 35, 34, 29, 28]
        indices_7 = [22, 24, 18, 21, 25, 23]
        indices_8 = [33, 34, 35, 23, 9, 31, 27]
        indices_9 = [37, 40, 32, 33, 41]
        scale_1_sum = calculator_service.sum_specific_elements(answers, indices_1)
        scale_2_sum = calculator_service.sum_specific_elements(answers, indices_2)
        scale_3_sum = calculator_service.sum_specific_elements(answers, indices_3)
        scale_4_sum = calculator_service.sum_specific_elements(answers, indices_4)
        scale_5_sum = calculator_service.sum_specific_elements(answers, indices_5)
        scale_6_sum = calculator_service.sum_specific_elements(answers, indices_6)
        scale_7_sum = calculator_service.sum_specific_elements(answers, indices_7)
        scale_8_sum = calculator_service.sum_specific_elements(answers, indices_8)
        scale_9_sum = calculator_service.sum_specific_elements(answers, indices_9)
        return scale_1_sum, scale_2_sum, scale_3_sum, scale_4_sum, scale_5_sum, scale_6_sum, scale_7_sum, scale_8_sum, scale_9_sum

    def test_back_calculate_results(self, answers: List[int]):
        indices_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        indices_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        indices_3 = [14, 15, 16, 17, 18, 19, 20, 21]
        scale_1_sum = calculator_service.sum_specific_elements(answers, indices_1)
        scale_2_sum = calculator_service.sum_specific_elements(answers, indices_2)
        scale_3_sum = calculator_service.sum_specific_elements(answers, indices_3)
        return scale_1_sum, scale_2_sum, scale_3_sum

calculator_service = Calculator()