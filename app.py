import requests

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data.get("type") == "single":
            return joke_data["joke"]
        else:
            return f"{joke_data['setup']} - {joke_data['delivery']}"
    else:
        return "Failed to fetch a joke. Please try again."

if __name__ == "__main__":
    print("Fetching a joke...")
    print(fetch_joke())
