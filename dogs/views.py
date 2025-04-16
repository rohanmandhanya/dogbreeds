import requests
import time
from django.shortcuts import render
from django.http import HttpRequest

API_URL = "https://interview-api-olive.vercel.app/api/dogs?page={}"
MAX_RETRIES = 3
TIMEOUT = 5

def fetch_dogs(page, retries=MAX_RETRIES):
    for attempt in range(retries):
        try:
            response = requests.get(API_URL.format(page), timeout=TIMEOUT)
            response.raise_for_status()
            data = response.json()

            # Validate response shape
            if isinstance(data, list) and all("breed" in dog for dog in data):
                return data, None
        except requests.RequestException as e:
            error_message = str(e)

        time.sleep(1 + attempt)

    return [], error_message if 'error_message' in locals() else "Unknown error"

def dog_list(request: HttpRequest):
    page = int(request.GET.get('page', 1))
    dogs_raw, error = fetch_dogs(page)

    context = {
        'dogs': dogs_raw,
        'page': page,
        'has_next': True, # this can control next button
        'has_prev': page > 1,
        'error': error,
    }
    return render(request, 'dogs/dog_list.html', context)
