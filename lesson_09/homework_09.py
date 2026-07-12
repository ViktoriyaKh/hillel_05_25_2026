class Romb:
    def __init__(self, storona_a, kut_a):
        self.storona_a = storona_a
        self.kut_a = kut_a

    def __setattr__(self, key, value):
        if key == 'storona_a':
            if value <= 0:
                print("storona_a повинна бути більше 0")
                return

        if key == 'kut_a':
            if not (0 < value < 180):
                print("kut_a повинен бути між 0 і 180")
                return
            super().__setattr__('kut_b', 180 - value)

        if key == 'kut_b':
            return

        super().__setattr__(key, value)
