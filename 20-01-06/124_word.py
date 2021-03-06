'''10진법	124 나라	10진법	124 나라
    1	     1	      6	      14
    2	     2	      7	      21
    3	     4	      8	      22
    4	     11	      9	      24'''
''' 문제 : 자연수 n이 매개변수로 주어질 때,n을 124 나라에서 사용하는 숫자로 
          바꾼 값을 return 하도록 solution 함수를 완성해 주세요. '''

#코드 
def solution(n):
    answer = ''
    while n > 0:
      n -= 1 #  index 때문에
      answer += '124'[n%3] + answer
      n //= 3
return answer
    
''' 느낀 점
    '문자열'[인덱스]  
    ex) '문자열'[0]  결과 값은 '문'
 //는 정수를 보여줌 
 / 는 소숫점까지 보여줍니다.
