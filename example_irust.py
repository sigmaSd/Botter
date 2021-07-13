#!/bin/python
from Botter import Bot
import time

# This example assumes an AZERTY keyboard
class MyBot(Bot.Bot):
    def bot(self):
        # LEFTMETA + ENTER is bound to spawn a new terminal on my pc
        with self.with_mod("KEY_LEFTMETA"):
            self.send_key("KEY_ENTER")

        # Wait for focus to shift to the new terminal
        time.sleep(1)  

        # Start IRust
        self.send_letters("irust")
        self.send_key("KEY_ENTER")

        # Insert 5 and click enter
        with self.with_mod("KEY_LEFTSHIFT"):
            self.send_letters("5")
            self.send_key("KEY_ENTER")


bot = MyBot()
bot.run()
