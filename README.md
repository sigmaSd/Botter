# Botter (linux evdev)

## Example
```python
from Botter import Bot

# This example assumes an AZERTY keyboard

class MyBot(Bot.Bot):
    def bot(self):
        # LEFTMETA + ENTER is bound to spawn a new terminal on my pc
        with self.with_mod("KEY_LEFTMETA"):
            # Wait for focus to shift to the new terminal
            self.send_key("KEY_ENTER", 1)

        # Echo
        self.send_keys("echo Hello Bot")
        self.send_key("KEY_ENTER", 0.05)


bot = MyBot()
bot.run()
```

### Credits
https://github.com/meeuw/injectinput
