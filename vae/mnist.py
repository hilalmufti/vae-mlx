import os


def join_path(xs):
    def go(xs, acc):
        match xs:
            case []:
                return acc
            case [x, *xs] if x.startswith("/") and acc != "":
                return x
            case [x, *xs]:
                return go(xs, acc + "/" + x)
            
    match xs:
        case []:
            raise ValueError("Must provide at least one path")
        case [x, *xs]:
            y = go(xs, x); assert y == os.path.join(*[x, *xs]), (y, os.path.join(*[x, *xs]))
            return y

def mnist(
    save_dir="/tmp",
    base_url="https://raw.githubusercontent.com/fgnt/mnist/master/",
    filename="mnist.pkl"
):
    return os.path.join(save_dir, filename)