import json
import os

import requests

DIR = os.path.dirname(os.path.abspath(__file__))
API_SERVER = "https://api.telegram.org/bot"


def load_config():
    try:
        with open(os.path.join(DIR, "config.json")) as config_json:
            config = json.load(config_json)
    except FileNotFoundError:
        print("No Config")
    return config["API_TOKEN"], config["UMEH_SERVER"], config["PORT"], config


API_TOKEN, UMEH_SERVER, PORT, CONFIG_DIC = load_config()


def config_update():
    try:
        with open(os.path.join(DIR, "config.json"), 'w+') as config_json:
            json.dump(CONFIG_DIC, config_json)
            config_json.close()
    except FileNotFoundError:
        print("No Config")


messages = []


def process_message():
    '''
            :var messages List
                Message list beginning with the latest message of last update
        '''

    '''
            Example:
            [
                {
                    'update_id' : 414331188,
                    'message' : {
                        'message_id'  4，
                        ‘from’ : {
                            'id' : 81632974,
                            'is_bot' : false
                            'first_name' : 'Kou',
                            'last_name' : 'Mei',
                            'username': 'KouMei',
                            'language_code' : 'zh-hans
                        },
                        'chat' : {
                            'id' : 81632974,
                            'is_bot' : false
                            'first_name' : 'Kou',
                            'last_name' : 'Mei',
                            'username': 'KouMei',
                            'type' : 'private'
                        },
                        date : 1614458067,
                        text : 'text'
                    }
                },
                {},{},{}...
            ]
    '''
    pass


'''
    :param offset Integer
        the newest message id in last update
'''




def get_updates():
    path = API_SERVER + API_TOKEN + "/getUpdates?offset=" + str(CONFIG_DIC["MESSAGE_ID"])
    r = requests.get(path)
    '''
        :var messages List
            Message list beginning with the latest message of last update
    '''

    '''
            Example:
            [
                {
                    'update_id' : 414331188,
                    'message' : {
                        'message_id'  4，
                        ‘from’ : {
                            'id' : 81632974,
                            'is_bot' : false
                            'first_name' : 'Kou',
                            'last_name' : 'Mei',
                            'username': 'KouMei',
                            'language_code' : 'zh-hans
                        },
                        'chat' : {
                            'id' : 81632974,
                            'is_bot' : false
                            'first_name' : 'Kou',
                            'last_name' : 'Mei',
                            'username': 'KouMei',
                            'type' : 'private'
                        },
                        date : 1614458067,
                        text : 'text'
                    }
                },
                {},{},{}...
            ]
    '''
    global messages
    messages = r.json()["result"]
    CONFIG_DIC["MESSAGE_ID"] = messages[len(messages) - 1]['update_id']
    config_update()


def main():
    get_updates()


if __name__ == '__main__':
    main()
