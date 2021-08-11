import re
import TermuxCustomBanner.colors as colors
import pyfiglet
from sys import exit
from subprocess import call

def clear():
    call('cls', shell=True)


def continue_prompt(text=''):
    '''
    prompts user if they wanna continue
    '''
    response = input(f'{colors.CYAN}Do you want to continue {text} {colors.RESET} {colors.YELLOW} (y/n){colors.RESET} (default: n): ').lower().strip()
    print()
    if response == 'y':
        return True
    return False


def set_font(text:str):
    '''
    get user choice font
    '''
    fonts = pyfiglet.FigletFont.getFonts()
    
    count = 0
    for font in fonts:
        print (f'{colors.YELLOW}[{count}] {font}{colors.RESET}\n')
        print(pyfiglet.figlet_format(text, font=font))
        count += 1
        if count % 5 == 0 and not continue_prompt('font search'):
                break
    try:
        user_font_index = int(input(f'{colors.YELLOW}[+] Enter font number : {colors.RESET}'))
        print(user_font_index, type(user_font_index))
        figlet_font = pyfiglet.figlet_format(text, font=fonts[user_font_index])
        print(figlet_font)
        if continue_prompt('with this font'):
            return figlet_font
        else:
            print(f'{colors.RED}[!] Exiting!!')
            exit()

    except Exception:
        print(f'{colors.RED}[!] No such font found. Exiting...{colors.RESET}')
        exit()



def get_color(text:str):
    colors_list = [colors.BLACK, colors.RED, colors.GREEN, colors.YELLOW, colors.BLUE, colors.MAGENTA, colors.CYAN, colors.LIGHT_GRAY]
    print(f'''
{colors.YELLOW}[0]{colors.RESET} {colors.BLACK}BLACK{colors.RESET}(BLACK)
{colors.YELLOW}[1]{colors.RESET} {colors.RED}RED{colors.RESET}
{colors.YELLOW}[2]{colors.RESET} {colors.GREEN}GREEN{colors.RESET}
{colors.YELLOW}[3]{colors.RESET} {colors.YELLOW}YELLOW{colors.RESET}
{colors.YELLOW}[4]{colors.RESET} {colors.BLUE}BLUE{colors.RESET}
{colors.YELLOW}[5]{colors.RESET} {colors.MAGENTA}MAGENTA{colors.RESET}
{colors.YELLOW}[6]{colors.RESET} {colors.CYAN}CYAN{colors.RESET}
{colors.YELLOW}[7]{colors.RESET} {colors.LIGHT_GRAY}LIGHT_GRAY{colors.RESET}
        ''')
    try:
        index = int(input(f'{colors.YELLOW}[+] Enter color number (default: 3): {colors.RESET}'))
        return colors_list[index]
    except Exception:
        return colors_list[3]


def get_font_with_style(message:str):
    response = input(message)
    updated_response = set_font(response)
    color = get_color(updated_response)
    return updated_response, color


def get_banner():
    head_str, head_color = get_font_with_style(f'{colors.YELLOW}[+] Enter Heading for banner : {colors.RESET}')
    text_str = input(f'{colors.YELLOW}[+] Enter text for banner : {colors.RESET}')
    text_color = get_color(text_str)
    banner = f'{head_color}{head_str}{colors.RESET}\n{text_color}{text_str}{colors.RESET}'
    return banner


def start():
    clear()
    banner = get_banner()
    print('Generated Banner')
    print(banner)