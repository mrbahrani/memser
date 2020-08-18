class MemWrite(object):
    def __init__(self):
        self.data = bytes()

    def write(self, stuff):
        self.data = stuff


class MemRead(object):
    def __init__(self, b: bytes):
        self.offset = 0
        self.b = b

    def read(self, size=None):
        offset = self.offset
        self.offset = self.offset + size
        return self.b[offset: offset+size]

    def readline(self):
        for b_i in range(self.offset, len(self.b)):
            if self.b[b_i] == 10:
                offset = self.offset
                self.offset = b_i + 1
                return self.b[offset: b_i + 1]
            offset = self.offset
        return self.b[offset: len(self.b)]
