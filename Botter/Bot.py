import evdev
import time
import contextlib


class Bot(evdev.UInput):
    ###############
    # Constructor #
    ###############
    def __init__(self):  # override
        super().__init__(evdev.util.find_ecodes_by_regex(
            r"KEY_([A-Z0-9]|SPACE|LEFTSHIFT|LEFTMETA|ENTER)$"))

    ###########
    # Private #
    ###########
    def _syn(self):  # override
        super().syn()
        time.sleep(0.05)

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
    def send_letters(self, keys):
        for key in keys:
            key = evdev.ecodes.ecodes["KEY_" + key.upper()]
            self.write(evdev.ecodes.EV_KEY, key, 1)
            self.write(evdev.ecodes.EV_KEY, key, 0)
        self._syn()
    def send_key(self, key):
        key = evdev.ecodes.ecodes[key]
        self.write(evdev.ecodes.EV_KEY, key, 1)
        self.write(evdev.ecodes.EV_KEY, key, 0)
        self._syn()
    def run(self):
        self.bot()
        self.close()

    ############################
    # Public: Required method  #
    ############################
    def bot(self):
        raise NotImplementedError
