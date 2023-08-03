def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return deco_func


import time

def sleep_for_a_while():
    print("sleeping ..")
    time.sleep(2)
    print("done sleeping")

sleep_for_a_while()
