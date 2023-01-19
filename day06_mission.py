#9.3
def test(func):
    def wrap():
        print('start')
        func()
        print('end')
    return wrap

@test
def f():
    print('하하')

f()

#9.4
class OopsException(Exception):
    pass
try:
    raise OopsException('oops')
except OopsException as exc:
    print(exc)