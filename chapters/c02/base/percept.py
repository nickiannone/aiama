class Percept:
    def __init__(self, *info):
        self.info = tuple(info)

    def __repr__(self):
        return f"Percept(info={self.info})"