class Simple(object):
    def __init__(self, x):
        self.x = x
        self.y = 6

    def get_x(self):
        return self.x


class WithCollection(object):
    def __init__(self):
        self.l = list()
        self.d = dict()

    def get_l(self):
        return self.l