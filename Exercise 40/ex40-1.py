class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there\n"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells\n"])
						
test = Song(["I have a test tomorrow",
			 "A math test!",
			 "No, it's actually a physics test.",
			 "See you later\n"])
			 
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

test.sing_me_a_song()
