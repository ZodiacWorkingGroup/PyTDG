class point:
    def __init__(self, *args):
        argt = [type(a) for a in args]

        if len(argt) == 2 and all([a in [int, float] for a in argt]):
            self.x = args[0]
            self.y = args[1]

        elif len(argt) == 1 and type(argt[0]) == complex:
            self.x = argt[0].real
            self.y = argt[0].imag

        elif len(argt) == 1 and type(argt[0]) == tuple and len(argt[0]) == 2:
            self.x = args[0][0]
            self.y = args[0][1]

    def translate(self, x=0, y=0):
        return point(self.x+x, self.y+y)

    def reflect_over(self, ln):
        pass

    def rotate_about(self, point, angle):
        pass

    def __add__(self, other):
        if type(other) == point:
            return point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        if type(other) == point:
            return point(self.x-other.x, self.y-other.y)


class segment:
    def __init__(self, a, b):
        self._start = a
        self._end = b

    def __len__(self):
        return distance(self._start, self._end)