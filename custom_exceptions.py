"""Errors"""

class BotNotFound(Exception):
    def __init__(self):
        self.message = "Robot not found!"

    def __str__(self):
        return self.message