import requests

def search_card(card_name):
    '''
        search card by name on skryfall api
        :param card_name: name of the card to search
        :return: json response
    '''
    request_url = "https://api.scryfall.com/cards/named?fuzzy="
    response = requests.get(request_url+card_name, timeout=5)
    return response.json()