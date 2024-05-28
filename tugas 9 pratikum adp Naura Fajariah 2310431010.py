import time
from colored import fore, back, style
def countdown(seconds):
    while seconds > 0:
        print(f"TIME TOO SEE OUR DESIGN: {seconds} detik", end="\r")
        time.sleep(1)
        seconds -= 1
    print("ENJOY!")

if __name__ == "__main__":
    countdown(5)

def print_colored_block(color):
    print(color + '  ' + style('reset'), end='')

def visa_logo():
    blue = back('blue')
    white = back('white')
    yellow = back('yellow')

    logo = [
        [blue] * 60,
        [blue] * 60,
        [white] * 60,
        [white] * 2 + [blue] * 4 + [white] * 15 + [blue] * 4 + [white] * 1 + [blue] * 3 + [white] * 1 + [blue] * 7 + [white] * 1 + [white] * 6 + [blue] * 3 + [white] * 13,
        [white] * 3 + [blue] * 4 + [white] * 13 + [blue] * 4 + [white] * 2 + [blue] * 3 + [white] * 1 + [blue] * 7 + [white] * 6 + [blue] * 2 + [white] * 1 + [blue] * 2 + [white] * 12,
        [white] * 5 + [blue] * 5 + [white] * 9 + [blue] * 4 + [white] * 3 + [blue] * 3 + [white] * 1 + [blue] * 1 + [white] * 6 + [white] * 5 + [blue] * 2 + [white] * 3 + [blue] * 2 + [white] * 11,
        [white] * 8 + [blue] * 4 + [white] * 6 + [blue] * 4 + [white] * 4 + [blue] * 3 + [white] * 1 + [blue] * 7 + [white] * 4 + [blue] * 2 + [white] * 5 + [blue] * 2 + [white] * 10,
        [white] * 9 + [blue] * 4 + [white] * 4 + [blue] * 4 + [white] * 5 + [blue] * 3 + [white] * 1 + [blue] * 7 + [white] * 3 + [blue] * 2 + [blue] *9 + [white] * 9,
        [white] * 10 + [blue] * 4 + [white] * 2 + [blue] * 4 + [white] * 6 + [blue] * 3 + [white] * 1 + [white] * 6 + [blue] * 1 + [white] * 2 + [blue] * 2 + [blue] * 11 + [white] * 8,
        [white] * 11 + [blue] * 4 + [blue] * 4 + [white] * 7 + [blue] * 3 + [white] * 1 + [blue] * 7 + [white] * 1 + [blue] * 2 + [white] * 11 + [blue] * 2 + [white] * 7,
        [white] * 60,
        [yellow] * 60,
        [yellow] * 60,
        


    ]

    for row in logo:
        for color in row:
            print_colored_block(color)
        print()

if __name__ == "__main__":
    visa_logo()