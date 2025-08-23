def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
    convert = float(d[1:])
    return convert


def percent_to_float(p):
    convert_percent = (float(p[:-1]))
    return convert_percent/100


def addthem(a, convert_percent=None):
    return convert_percent/100 +10

main()