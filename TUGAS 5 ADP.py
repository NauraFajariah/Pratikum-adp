import math

while True:
    n = int(input("Input banyak data n = "))
    x = []

    for i in range(n):
        x.append(int(input(f"Input nilai x ke-{i+1} = ")))

    print("No\tX\tf(x)\tg(x)\th(x)")
    for i in range(n):
        if x[i] > 0:
            fx = 3*x[i]*x[i] + 7*x[i]
            gx = 2*x[i]*x[i] - 5*x[i]
            hx = fx * gx
        else:
            fx = 4
            gx = math.pow((3*x[i]*x[i]+7*x[i]), 2) - math.sqrt(3*x[i]*x[i]+7*x[i])
            hx = 4 * (math.pow((3*x[i]*x[i]+7*x[i]), 2) - math.sqrt(3*x[i]*x[i]+7*x[i]))

        print(f"{i+1}\t{x[i]}\t{fx}\t{gx}\t{hx}")

    again = input("Input nilai x lagi? Y/N ")
    if again.upper() != 'Y':
        break
