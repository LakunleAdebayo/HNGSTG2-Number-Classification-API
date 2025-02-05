from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import math

def is_armstrong(num):
    # worked on the negative numbers as they cannot be Armstrong numbers
    if num < 0:
        return False
    num_str = str(abs(num))
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)

def is_prime(num):
    # changed to so that negative numbers cannot be prime numbers
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(abs(num))) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    # i think this will be help with negative numbers as they cannot be perfect numbers 
    if num <= 1:
        return False
    sum_divisors = sum(i for i in range(1, abs(num)) if abs(num) % i == 0)
    return sum_divisors == abs(num)

def get_digit_sum(num):
    # this will help with negative numbers by using absolute value
    return sum(int(digit) for digit in str(abs(num)))

def get_number_properties(num):
    properties = []
    
    if is_armstrong(num):
        properties.append("armstrong")
    
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    return properties

def get_fun_fact(num):
    try:
        response = requests.get(f'http://numbersapi.com/{num}/math')
        if response.status_code == 200:
            return response.text
        return f"{num} is an interesting number with various mathematical properties."
    except:
        return f"{num} is an interesting number with various mathematical properties."

@api_view(['GET'])
def classify_number(request):
    try:
        number = request.GET.get('number')
        if not number:
            return Response(
                {"number": None, "error": True},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        number = int(number)
        properties = get_number_properties(number)
        
        response_data = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": get_digit_sum(number),
            "fun_fact": get_fun_fact(number)
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    except ValueError:
        return Response(
            {"number": number, "error": True},
            status=status.HTTP_400_BAD_REQUEST
        )