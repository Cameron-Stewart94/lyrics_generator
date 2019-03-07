from ask_user_input import ask_user, ask_user_again
from song_lyrics import lyrics
from time import sleep

def run_programme():
    # Funtion to run the programme

    method_options = {
    'Print Lyrics' : ['1', 'print', 'print_lyrics'],
    'Save as text file' : ['2', 'text', 'text file', 'save as text file' , 'txt'],
    'Save as mp3 file' : ['3', 'mp3', 'mp3 file', 'save as mp3 file'],
    'Quit' : [4, 'Q', 'Quit', 'Exit']
    }

    with open('menus/main_menu.txt', 'r') as menu_file:
        menu = [line for line in menu_file]

    user_choices = ask_user()
    song_lyrics_generator = lyrics(user_choices['Artist'], user_choices['Song'])

    try:
        song_lyrics_generator.fetch_data()
    except:
        try_again = input('Invalid choice, try again? ').lower()
        if try_again == 'y' or try_again == 'Y':
            run_programme()
    else:
        quit = False
        while quit == False:
            print(song_lyrics_generator)
            sleep(1)
            print(*menu)
            menu_choice = input()

            if menu_choice in method_options['Print Lyrics']:
                song_lyrics_generator.print_lyrics()

            elif menu_choice in method_options['Save as text file']:
                song_lyrics_generator.write_to_txt_file()

            elif menu_choice in method_options['Save as mp3 file']:
                song_lyrics_generator.write_to_mp3_file()

            elif menu_choice in method_options['Quit']:
                quit = True





    """user_choices = ask_user()
    song_lyrics_generator = lyrics(user_choices['Artist'], user_choices['Song'])
    # Creates instance of song_lyrics_generator

    try:
        song_lyrics_generator.fetch_data()
    except:
        print('Invalid choice, try again...')
        run_programme()
    else:
        print(song_lyrics_generator)

        song_lyrics_generator.write_to_txt_file()
        # Writes song to text file

        song_lyrics_generator.write_to_mp3_file()
        # Writes song to mp3 file

        another_song = ask_user_again()
        # Asks user if they would like to choose another song

        if another_song == True:
            run_programme()
            # Runs Programme again if user asks it to
            """


run_programme()
