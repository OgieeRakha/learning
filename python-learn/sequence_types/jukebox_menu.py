from challenge_nested import albums

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate (albums):
        print(index + 1, title)
    ans = int(input("pick one: "))
    if ans in [1,2,3,4,5,6,7,8]:
        for num, songs in (albums[ans-1][3]):
            print(str(num) + ". " + songs)
        ans_song = (int(input("pick one: ")))
        print("playing track number {0} song {1}"
              .format(ans_song, albums[ans-1][3][ans_song-1][1]))
        print("-"*50)
    else:
        print("Thank you for playing our jukebox")
        break