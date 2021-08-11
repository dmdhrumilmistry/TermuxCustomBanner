import TermuxCustomBanner.colors as colors
import pyfiglet
from sys import exit
from subprocess import call
from os import remove
from os.path import exists


COLOR_MENU = f'''
{colors.YELLOW}[0]{colors.RESET} {colors.BLACK}BLACK{colors.RESET}(BLACK)
{colors.YELLOW}[1]{colors.RESET} {colors.RED}RED{colors.RESET}
{colors.YELLOW}[2]{colors.RESET} {colors.GREEN}GREEN{colors.RESET}
{colors.YELLOW}[3]{colors.RESET} {colors.YELLOW}YELLOW{colors.RESET}
{colors.YELLOW}[4]{colors.RESET} {colors.BLUE}BLUE{colors.RESET}
{colors.YELLOW}[5]{colors.RESET} {colors.MAGENTA}MAGENTA{colors.RESET}
{colors.YELLOW}[6]{colors.RESET} {colors.CYAN}CYAN{colors.RESET}
{colors.YELLOW}[7]{colors.RESET} {colors.LIGHT_GRAY}LIGHT_GRAY{colors.RESET}
'''


def clear():
    '''
    clears screen
    '''
    call('clear', shell=True)


def exit_program():
    '''
    exits program
    '''
    print(f'{colors.RED}[!] Exiting!!')
    exit()


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
        figlet_font = pyfiglet.figlet_format(text, font=fonts[user_font_index])
        print(figlet_font)
        if continue_prompt('with this font'):
            return figlet_font
        else:
            exit_program()

    except Exception:
        print(f'{colors.RED}[!] No such font found.{colors.RESET}')
        exit_program()



def get_color(text:str):
    '''
    returns color
    '''
    colors_list = [colors.BLACK, colors.RED, colors.GREEN, colors.YELLOW, colors.BLUE, colors.MAGENTA, colors.CYAN, colors.LIGHT_GRAY]
    print(COLOR_MENU)
    try:
        index = int(input(f'{colors.YELLOW}[+] Enter color number (default: 3): {colors.RESET}'))
        color = colors_list[index]
        print(f'{color}{text}{colors.RESET}')
        if continue_prompt('with this color'):
            return color
        else:
            exit_program()

    except Exception:
        return colors_list[3]


def get_font_with_style(message:str):
    '''
    returns message in font style and color
    '''
    response = input(message)
    updated_response = set_font(response)
    color = get_color(updated_response)
    return updated_response, color


def get_banner():
    '''
    creates banner
    '''
    head_str, head_color = get_font_with_style(f'{colors.YELLOW}[+] Enter Heading for banner : {colors.RESET}')
    text_str = input(f'{colors.YELLOW}[+] Enter text for banner : {colors.RESET}')
    text_color = get_color(text_str)
    banner = f'{head_color}{head_str}{colors.RESET}\n{text_color}{text_str}{colors.RESET}'
    return banner


def start():
    '''
    starts creating banner
    '''
    clear()
    banner = get_banner()

    clear()
    print(f'{colors.YELLOW}[*] Banner Preview:{colors.RESET}')
    print(banner)

    if continue_prompt('with this banner'):
        print(f'{colors.YELLOW}[*] Generating Files...{colors.RESET}')
        SH_data = f'#!/bin/bash\n\necho -e "\n{banner}\n"'
        
        # remove motd if exists
        if exists('/data/data/com.termux/files/usr/etc/motd'):
            remove('/data/data/com.termux/files/usr/etc/motd')

        # create new shell script to run when terminal is used
        with open('/data/data/com.termux/files/usr/etc/profile.d/TermuxCustomBanner.sh', 'w') as motd:
            motd.write(SH_data)
        print(f'{colors.YELLOW}[*] Banner has been applied.{colors.RESET}')

    else:
        exit_program()