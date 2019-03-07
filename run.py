from ask_user_input import ask_user, ask_user_again
from song_lyrics import lyrics
from time import sleep
from method_options import method_options

def run_programme():
    # Funtion to run the programme

    with open('menus/main_menu.txt', 'r') as menu_file:
        menu = [line for line in menu_file]
    # Opens main menu text file and stores each line in a list

    user_choices = ask_user()
    song_lyrics_generator = lyrics(user_choices['Artist'], user_choices['Song'])
    # Asks user for artisit and song choice and creates instance of song lyrics generator class using the user's inputs

    try:
        song_lyrics_generator.fetch_data()
    except:
        try_again = input('Invalid choice, try again? ').lower()
        if try_again == 'y' or try_again == 'Y':
            run_programme()
        # Attemps to fetch song data from the web, if invalid choice is entered, the programme asks the user to try again
    else:
        while True:

            print('')
            print(menu[0])
            sleep(1)
            print(song_lyrics_generator)
            sleep(1)
            print(*menu[2: ])

            menu_choice = input().lower()

            if menu_choice in method_options['Print Lyrics']:
                print('Printing Lyrics...')
                sleep(1)
                print(song_lyrics_generator.print_lyrics())


            elif menu_choice in method_options['Save as text file']:
                song_lyrics_generator.write_to_txt_file()

            elif menu_choice in method_options['Save as mp3 file']:
                song_lyrics_generator.write_to_mp3_file()

            elif menu_choice in method_options['Choose another song']:
                run_programme()

            elif menu_choice in method_options['Quit']:
                break

run_programme()
