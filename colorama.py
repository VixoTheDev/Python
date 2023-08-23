from colorama import Fore, Back, Style, init

# Initialize Colorama on Windows
init(autoreset=True)

print(Fore.RED + "This text is red.")
print(Fore.GREEN + "This text is green.")
print(Fore.BLUE + "This text is blue.")

print(Back.YELLOW + Fore.BLACK + "Yellow background with black text.")
print(Back.CYAN + Fore.WHITE + "Cyan background with white text.")

print(Style.BRIGHT + "This text is bright.")
print(Style.DIM + "This text is dim.")

print(Style.RESET_ALL + "Back to default styles.")
