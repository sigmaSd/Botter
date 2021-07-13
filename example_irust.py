#!/bin/python
from Botter import Bot
import time

# This example assumes an AZERTY keyboard


class MyBot(Bot.Bot):
    def bot(self):
        # LEFTMETA + ENTER is bound to spawn a new terminal on my pc
        with self.with_mod("KEY_LEFTMETA"):
            # Wait for focus to shift to the new terminal
            self.send_key("KEY_ENTER", 1)

        # Start IRust
        self.send_keys("irust")
        # Wait a bit so the LEFTSHIFT modifier isn't set too soon
        self.send_key("KEY_ENTER", 0.05)

        # Insert 5 and click enter
        with self.with_mod("KEY_LEFTSHIFT"):
            self.send_keys("5 + 4", 0.01)
            self.send_key("KEY_ENTER")


bot = MyBot()
bot.run()
