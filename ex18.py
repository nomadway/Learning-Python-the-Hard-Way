

def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}.")


def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}.")


def print_one(arg1):
	print(f"arg1:{arg1}")

def print_nothing():
	print("Nothing")



print_two("Turdu", "Salamat")
print_two_again("Turdu-Ata", "Salamat-Apa")
print_one("Turdu")
print_nothing()