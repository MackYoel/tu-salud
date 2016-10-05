import pprint


def _pprint(var, label=None):
    pp = pprint.PrettyPrinter(indent=4)
    if label is not None:
        print('+' * 10, label.upper(), '+' * 10)
    else:
        print('+' * 20)
    pp.pprint(var)
    print()
