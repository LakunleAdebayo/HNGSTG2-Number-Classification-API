from django.shortcuts import render
import requests
from math import sqrt

from django.http import JsonResponse
from rest_framework.decorators import api_view

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@api_view(["GET"])
def classify_number(request):
    number = request.GET.get("number")

    try:
        number = int(number)
    except (TypeError, ValueError):
        return JsonResponse({"number": number, "error": True}, status=400)

    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.insert(0, "armstrong")

    response = requests.get(f"http://numbersapi.com/{number}/math", timeout=5)
    fun_fact = response.text if response.status_code == 200 else "No fun fact available."

    data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": False,
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": fun_fact,
    }
    return JsonResponse(data)
