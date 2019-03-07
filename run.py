from ask_user_input import ask_user, ask_user_again
from song_lyrics import lyrics

def run_programme():
    # Funtion to run the programme

    with open('menus/main_menu.txt', 'r') as menu_file:
        options = [line for line in menu_file]
        print(options)


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
