class Additor:
    @staticmethod
    def add(a, b):
        return a + b

    def bar(self):
        return self.Inner()

    class Inner:
        def foo():
            print('hi')
