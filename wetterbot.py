#!/usr/bin/python3

import os

import toml
import peewee

import telegram_api.telegram_bot_api as api
import weewx_dbmodel
import wetterbot_dbmodel


def load_config():
    configfile = os.path.join(SKRIPTPFAD, "config.toml")
    with open(configfile) as conffile:
        config = toml.loads(conffile.read())
    return config


SKRIPTPFAD = os.path.abspath(os.path.dirname(__file__))
CONFIG = load_config()

LOGGER = None

BOT = api.Bot(CONFIG["token"])


class Account:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.mode = None
        self.umode = None
        self.benachrichtigungen = {}

        # c = commands
        self.bot_kommandos = {"/start": self.c_start,
                              "/help": self.c_help,
                              "/acc_loeschen": self.c_acc_loeschen,
                              "/benachrichtigungen": self.c_benachrichtigungen,
                              "/alarme": self.c_alarme,
                              "/abbrechen": self.c_abbrechen}

    def add_benachrichtigung(self, ts_next_nachricht, typ, inhalt_konfiguration, intervall_nachricht):
        self.benachrichtigungen[typ] = {"ts_next_nachricht": ts_next_nachricht,
                                        "inhalt_konfiguration": inhalt_konfiguration,
                                        "intervall_nachricht": intervall_nachricht}

    def bot_kommando_aufrufen(self, nachricht):
        kommando = nachricht["message"]["text"]
        try:
            self.bot_kommandos[kommando](nachricht)
        except KeyError:
            BOT.send_message(self.chat_id, "Botkommando {} unbekannt".format(kommando))

    def c_start(self, nachricht):
        pass

    def c_help(self, _):
        with open("botkommandos.txt", encoding="UTF-8") as file:
            inhalt = file.readlines()
            ausgabe = "".join(inhalt)
        BOT.send_message(self.chat_id, ausgabe)

    def c_acc_loeschen(self, nachricht):
        pass

    def c_benachrichtigungen(self, nachricht):
        pass

    def c_alarme(self, nachricht):
        pass

    def c_abbrechen(self, nachricht):
        pass


class Benachrichtigungen:
    """
    Benötigtes queue Format: (zeit_der_versendung, accountobjekt)
    """
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def sorting_queue(self):
        self.queue.sort()

if __name__ == "__main__":
    test_acc = Account(CONFIG["test_id"])
    test_acc.c_help("a")
        #if nachricht["message"]["entities"][0]["type"] == "bot_command":



