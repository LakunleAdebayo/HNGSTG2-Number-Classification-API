from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import math

def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    if num <= 1:
        return False
    sum_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_divisors == num

def get_digit_sum(num):
    return sum(int(digit) for digit in str(num))

def get_number_properties(num):
    properties = []
    
    # Check Armstrong
    if is_armstrong(num):
        properties.append("armstrong")
    
    # Check parity
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
