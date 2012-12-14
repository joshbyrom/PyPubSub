class PubSub(object):
    def __init__(self):
        self.handlers = {}

    def on(self, event, fun):
        if not event in self.handlers:
            self.handlers[event] = []

        self.handlers[event].append(fun)

    def emit(self, event, *args):
        if event in self.handlers:
            for fun in self.handlers[event]:
                fun(self, *args)


if __name__ == '__main__':
    ps = PubSub()

    # In Python 2.x, print is a statement.
    # Lambda's need expressions, so I wrapped the print statement in a function.
    def printAsFunction(x):
        print 'I was told to say', ''.join([x, '.'])
        
    ps.on('Say', lambda x, args: printAsFunction(args))

    ps.emit('Say', 'Hello')
