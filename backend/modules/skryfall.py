import requests

def match_card(card_name, set: str = None):
    '''
        search card by name on skryfall api
        :param card_name: name of the card to search
        :return: json response
    '''
    request_url = f"https://api.scryfall.com/cards/named?fuzzy="
    if set:
        request_url += f"&set={set}"
    response = requests.get(request_url+card_name, timeout=20)
    return response.json()

def fetch_card_info(skryfall_id: str):
    '''
        fetch card info by id on skryfall api
        :param card_id: skryfall id of the card to search
        :return: json response
    '''
    request_url = f"https://api.scryfall.com/cards/{skryfall_id}"
    response = requests.get(request_url, timeout=20)
    return response.json()
