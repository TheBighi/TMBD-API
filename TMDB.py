import requests

while True:
    try:
        question = int(input("Do you want to get info based on now playing, popular, top rated or upcoming movies [1, 2, 3, 4]: "))
        if question in [1, 2, 3, 4]:
            break
        else:
            print("Enter number")
    except ValueError:
        print("Number please.")

if question == 1:
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer APIKEY HERE HAS TO BE (API Read Access Token) NOT (API key) FOR SUM REASON"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

if question == 2:
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjJhNjM4N2ViZWY3OWI2ZjlmMDU5N2Y2MDFiOGEzZSIsIm5iZiI6MTc0MjQ4OTA4My43MTUwMDAyLCJzdWIiOiI2N2RjNDVmYjBkMzM5YmI3MTQ3ZmM0YmIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.5bvm-ylN6s8_BOE6vSz-mSBox-hWdRax1l4IcxLFNoo"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

if question == 3:
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjJhNjM4N2ViZWY3OWI2ZjlmMDU5N2Y2MDFiOGEzZSIsIm5iZiI6MTc0MjQ4OTA4My43MTUwMDAyLCJzdWIiOiI2N2RjNDVmYjBkMzM5YmI3MTQ3ZmM0YmIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.5bvm-ylN6s8_BOE6vSz-mSBox-hWdRax1l4IcxLFNoo"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

if question == 4:
    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YjJhNjM4N2ViZWY3OWI2ZjlmMDU5N2Y2MDFiOGEzZSIsIm5iZiI6MTc0MjQ4OTA4My43MTUwMDAyLCJzdWIiOiI2N2RjNDVmYjBkMzM5YmI3MTQ3ZmM0YmIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.5bvm-ylN6s8_BOE6vSz-mSBox-hWdRax1l4IcxLFNoo"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

#print(response.text)

for movie in data["results"]:
    print("")
    print(f"\033[92m Title: {movie["original_title"]} \033[0m")
    print(f"Description: {movie["overview"]}")

