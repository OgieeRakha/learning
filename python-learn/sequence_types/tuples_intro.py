albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))
for album, artist, year in albums:
    print("Album {0} by {1} from {2}"
          .format(album, artist, year))
print("-"*50)
for album in albums:
    name, artist, year = album
    print("Album {0} by {1} from {2}"
           .format(album, artist, year))
