def main():

    def sum(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def dia(x, y):
        if y != 0:
            return x / y
        else:
            return None

    while True:
        calculate = input("Give sum, sub, mul or dia")
        if calculate is "sum":
            print(sum())



