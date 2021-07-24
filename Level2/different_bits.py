def solution(numbers):
     answer = [] 
     for number in numbers:
         if number % 2 == 0: 
             binary_num = list(bin(number)[2:]) 
             binary_num[-1] = "1" 
         else: 
             binary_num = bin(number)[2:] 
             binary_num = "0" + binary_num 
             one_idx = binary_num.rfind("0") 
             binary_num = list(binary_num) 
             binary_num[one_idx] = "1" 
             binary_num[one_idx + 1] = "0" 
         ans_num = int("".join(binary_num), 2) 
         answer.append(ans_num) 
     return answer 

