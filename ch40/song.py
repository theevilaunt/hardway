class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

lyric1 = ["Happy birthday to you",
"You live in a zoo",
"You look like a monkey"]

lyric2 = ["They rally round the family",
"With pockets full of shells"]

hbday = Song(lyric1)

bparade = Song(lyric2)

hbday.sing_me_a_song()
bparade.sing_me_a_song()