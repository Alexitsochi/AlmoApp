import json
import requests
from requests.exceptions import HTTPError

with open("Sites.json", "r") as sites:
    Site = json.load(sites)


def ping_almo():

    for url in [Site["almo"]]:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError:
            resp = "Алмо не доступна"
        except Exception:
            resp = "Алмо не доступна"
        else:
            resp = "Алмо доступна"

    return resp


if __name__ == "__main__":
    ping_almo()
