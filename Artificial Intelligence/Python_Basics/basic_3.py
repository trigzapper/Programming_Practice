def f1_team(team_name , racer_name):
    for i in range(len(team_name)):
        print(f"Team: {team_name[i]} , Racer: {racer_name[i]}")


def laptop_list(size, *company , **specs):
    print(f"Size of laptop: {size}")
    print(f"Company: {company}")
    print(f"Specifications: {specs}")

square_lambda = lambda n: n**2

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def shout(x):
    return x.upper()

def process_text(func , word ):
    return func(word)


#team = ["redbull", "ferrari", "mclaren", "mercedes", "alpine"]
#racers = ["verstappen", "leclerc", "norris", "hamilton", "ocon"]
#f1_team(racer_name = racers , team_name = team)

#laptop_list(14, "dell", "hp", "lenovo", "macbook" , "razer" , ram = "16GB", storage = "1TB", processor = "i7 or equivalent" , ports = "2 USB 3.0, 1 USB-C, 1 HDMI, 1 Audio Jack")

#print(square_lambda(7))

#print(factorial(4))

yell = shout
print(yell("Hellloooo"))

print(process_text( shout , "Holaaa "))
