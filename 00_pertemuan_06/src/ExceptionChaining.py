try:
    open('database.sqlite')
except IOError:
    raise RuntimeError from None