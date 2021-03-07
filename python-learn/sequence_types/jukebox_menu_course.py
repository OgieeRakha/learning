from challenge_nested import albums
#we use all capital in a word to make sure that
#the variable is a constant and we may not change it
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate (albums):
        print("{} : {}"
              .format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break
    print("Please choose your song:")
    for index, (number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        continue
    print("Playing {}".format(title))
    print("=" * 40)
