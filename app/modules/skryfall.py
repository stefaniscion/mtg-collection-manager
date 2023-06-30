import requests

def match_card(card_name, set: str = None):
    '''
        search card by name on skryfall api
        :param card_name: name of the card to search
        :return: json response
    '''
    request_url = "https://api.scryfall.com/cards/named?fuzzy="
    if set:
        request_url += f"&set={set}"
    response = requests.get(request_url+card_name, timeout=20)
    return response.json()
