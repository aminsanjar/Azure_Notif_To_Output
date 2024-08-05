import requests
import codecs
from flask import jsonify
import traceback

# server_url = "http://10.0.0.24:14125/"
server_url = "https://localhost:14125/"

# master_server
api_key = "U4D073463OS6LSO015MT6P8S86S8QK36"

# test_server
# api_key = "C3RUO878EP02138GF81YW5247GBTD4MP"


def send_notif(user_name, message):
    print(
        "---------------------------------[Send Notif to Outpute]--------------------------------")
    print("\n")
    if user_name == None or "":
        user_name = "sanjarmoosavi-m"
    b = {
        "from": "AZURE",
        "to": user_name,
        "message": message,
        "color": "C7EDFC",
        "otr": "0",
        "notify": "1"
    }
    try:
        response = requests.post(
            f"{server_url}/api/notify",
            headers={"API-KEY": f"{api_key}",
                     "Content-Type": "application/json"},
            json=b)
        print(response)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        error_dict = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        return jsonify({"successfully": False, "message": "There was an HTTP error sending the request to Output ", "error": error_dict})
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        error_dict = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        return jsonify({"successfully": False, "message": "There was an error sending the request to Output ", "error": error_dict})
    else:
        if response.status_code == 200:
            print("Message sent successfully.")
            return jsonify({"successfully": True, "message": "Message sent successfully."})
        else:
            print(f"Error sending message: {response.status_code}")
            return jsonify({"successfully": False, "message": response.status_code, "error": response.json()})
    finally:
        print("\n")
        print("----------------------------------------------------------------------------------------")
