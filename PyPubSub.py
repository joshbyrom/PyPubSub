class PubSub(object):
    def __init__(self):
        self.handlers = {}

    def on(self, event, fun):
        if not event in self.handlers:
            self.handlers[event] = []

        self.handlers[event].append(fun)

    def emit(self, event, args=[]):
        if event in self.handlers:
            for fun in self.handlers[event]:
                fun(self, event, args)


if __name__ == '__main__':
    ps = PubSub()

    # In Python 2.x, print is a statement.
    # Lambda's need expressions, so I wrapped the print statement in a function.
    def printAsFunction(emitter, event, args):
        print emitter, 'was told to', event, ''.join([' '.join(args), '.'])
        
    ps.on('say', lambda emitter, event, args: printAsFunction(emitter, event, args or ["nothing"]))

    ps.emit('say', ['hello'])

    ps.emit('say') # no args
    
    ps.emit('Something you are not prepared for')
    ps.emit('Something you are not prepared for', ['with arguments'])


    # 12/14/2012: prints:
    # <__main__.PubSub object at 0x09749D30> was told to say hello.
    # <__main__.PubSub object at 0x09749D30> was told to say nothing.
