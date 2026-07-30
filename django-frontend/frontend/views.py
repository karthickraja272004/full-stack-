import requests
from django.conf import settings
from django.shortcuts import render


def all_users(request):
    try:
        print("=" * 50)
        print("Inside all_users()")
        print("BACKEND_URL:", settings.BACKEND_URL)

        response = requests.get(settings.BACKEND_URL + "/users")

        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        data = response.json()

        print("JSON Data:", data)

        context = {
            "users": data["users"]
        }

        return render(request, "home.html", context)

    except Exception as e:
        print("ERROR in all_users():", repr(e))
        raise


def user_detail(request, user_id):
    try:
        print("=" * 50)
        print("Inside user_detail()")
        print("BACKEND_URL:", settings.BACKEND_URL)

        response = requests.get(f"{settings.BACKEND_URL}/users/{user_id}")

        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        data = response.json()

        print("JSON Data:", data)

        context = {
            "user": data
        }

        return render(request, "user_detail.html", context)

    except Exception as e:
        print("ERROR in user_detail():", repr(e))
        raise