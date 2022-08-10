import ctypes
import colorama  # https://pypi.org/project/colorama/


def printc(text, color='white'):
    colorama.init()
	
	# Python interpreter doesn't enable the processing of ANSI escape sequences
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    color = color.lower()
    bright = colorama.Style.BRIGHT

    use = {'fire': colorama.Fore.RED,
           'earth': colorama.Fore.GREEN,
           'water': colorama.Fore.BLUE,
           'wood': colorama.Fore.YELLOW,
           'metal': colorama.Fore.CYAN,
		   'error': colorama.Fore.MAGENTA}

    if color == 'white':
        print(f'{text}')
    else:
        text_color = use[color]
        print(f'{bright}{text_color}{text}{colorama.Style.RESET_ALL}')


message = ('Type the year you want to check [Q to quit): ')

element = {
    0: ('Yang', 'Metal'),
    1: ('Yin', 'Metal'),
    2: ('Yang', 'Water'),
    3: ('Yin', 'Water'),
    4: ('Yang', 'Wood'),
    5: ('Yin', 'Wood'),
    6: ('Yang', 'Fire'),
    7: ('Yin', 'Fire'),
    8: ('Yang', 'Earth'),
    9: ('Yin', 'Earth')
}

animal = {
    0: 'Rat',
    1: 'Ox',
    2: 'Tiger',
    3: 'Rabbit',
    4: 'Dragon',
    5: 'Snake',
    6: 'Horse',
    7: 'Goat',
    8: 'Monkey',
    9: 'Rooster',
    10: 'Dog',
    11: 'Pig'
}

reference_year = 1924  # From https://en.wikipedia.org/wiki/Chinese_zodiac

print('Welcome to Chinese zodiac checker.\n')

while True:
    year = input(message)

    if year.lower() == 'q':
        raise SystemExit

    try:
        year_num = int(year)
    except ValueError:
        printc('Integers only!\n', 'error')
        continue

    remainder = (year_num - reference_year) % 12
	
    
    """ Technically it should be associated elements (Yin/Yang + 
    metal/water/wood/fire/earth) and associated animal but combination
    of element and animal sounds much cooler """

    year_element = element[int(year[-1])]
    year_animal = animal[remainder]	

    printc(
        f'\n{year_num} is the year of {year_element[1]} {year_animal} '
        f'({year_element[0]})\n', year_element[1])
