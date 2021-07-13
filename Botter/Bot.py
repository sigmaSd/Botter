import evdev
import time
import contextlib


class Bot(evdev.UInput):
    ###############
    # Constructor #
    ###############
    def __init__(self):  # override
        super().__init__(evdev.util.find_ecodes_by_regex(r"KEY_(.*)$"))

    ###########
    # Private #
    ###########
    def _syn(self, delay):  # override
        super().syn()
        time.sleep(delay)

    def _set_meta(self, key):
        key = evdev.ecodes.ecodes[key]
        self.write(evdev.ecodes.EV_KEY,  key, 1)

    def _unset_meta(self, key):
        key = evdev.ecodes.ecodes[key]
        self.write(evdev.ecodes.EV_KEY, key, 0)

    ############################
    # Public: Provided methods #
    ############################
    @contextlib.contextmanager
    def with_mod(self, mod):
        self._set_meta(mod)
        yield  # code will run here
        self._unset_meta(mod)

    def send_keys(self, keys, delay=0.0):
        for key in keys:
            if key == " ":
                self.send_key("KEY_SPACE", delay)
            elif key == "+":
                self.send_key("KEY_KPPLUS", delay)
            else:
                self.send_key("KEY_" + key.upper(), delay)
        self._syn(delay)

    def send_key(self, key, delay=0.0):
        key = evdev.ecodes.ecodes[key]
        self.write(evdev.ecodes.EV_KEY, key, 1)
        self.write(evdev.ecodes.EV_KEY, key, 0)
        self._syn(delay)

    def run(self):
        self.bot()
        self.close()

    ############################
    # Public: Required method  #
    ############################
    def bot(self):
        raise NotImplementedError
