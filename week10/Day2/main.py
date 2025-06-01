import csv
import requests
import json

url="https://jsonplaceholder.typicode.com/users"

def fetch_data(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=json.loads(response.text)
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"General request error: {e}")
    else:
        with open("users.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["ID", "Name", "Username", "Email", "City"])
        
            for user in data:
                writer.writerow([
                user["id"],
                user["name"],
                user["username"],
                user["email"],
                user["address"]["city"]
            ])
            print("CSV file 'users.csv' written successfully.")

if __name__ == "__main__":
    fetch_data(url)