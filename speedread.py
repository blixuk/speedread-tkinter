# file: speedread-terminal/speedread.py

import time
import os
import tkinter

class SpeedRead:

	def __init__(self, file:str, words_per_minute:int, word_focus:bool, word_delay:bool, punctuation_delay:bool, height:int, width:int, font_size:int) -> None:
		self.height = height
		self.width = width
		self.words_per_minute = words_per_minute
		self.word_focus = word_focus
		self.word_delay = word_delay
		self.punctuation_delay = punctuation_delay
		if font_size == None:
			self.font_size  = int(height / 2)
		else:
			self.font_size = font_size
		self.font = 'Courier'
		self.background_colour = 'White'
		self.focus_colour = 'Red'

		self.root = tkinter.Tk()
		self.root.title("SpeedRead")
		self.canvas = tkinter.Canvas(self.root, height=self.height, width=self.width)
		self.canvas.pack()
		self.canvas['bg'] = self.background_colour
		self.root.attributes('-type', 'dialog')
		self.root.after(300, self.read, self.open_file(file))
		tkinter.mainloop()

	def read(self, file) -> None:
		for word in file.split():
			word_index = self.get_word_index(word)
			word_padding = self.get_word_padding(word, word_index)
			word_delay = self.get_word_delay(word)

			self.canvas.create_rectangle(0, 0, self.width, self.height, fill = self.background_colour)
			self.canvas.create_text(self.width / 2, self.height / 2, text = word_padding, font = (self.font, self.font_size))
			if self.word_focus:
				self.canvas.create_text(self.width / 2, self.height / 2, text = word[word_index], font = (self.font, self.font_size), fill = self.focus_colour)
			self.root.update()

			time.sleep(self.get_word_delay(word))
		exit(0)


	def get_word_padding(self, word: str, index: int) -> int:
		if len(word) >1:
			number_to_left = index
			number_to_right = len(word) - (index + 1)
			if number_to_left < number_to_right:
				word = " " * (number_to_right - number_to_left) + word
			elif number_to_left > number_to_right:
				word = word + " " * (number_to_left - number_to_right)
		return word

	def get_word_index(self, word: str) -> int:
		word_length = len(word)
		if word_length <= 1:
			return 0
		elif 2 <= word_length <= 5:
			return 1
		elif 6 <= word_length <= 9:
			return 2
		elif 10 <= word_length <= 13:
			return 3
		else:
			return 4

	def get_word_delay(self, word: str) -> float:
		if self.word_delay:
			delay_factor = ((1 / float(self.words_per_minute) * 60) + (len(word) / 30))
		else:
			delay_factor =((1 / float(self.words_per_minute) * 60))

		punctuation_delay_factor = {',':2.0, ';':2.0, '...':5.0, '.':2.5, '!':2.5, ':':2.5, '?':3.0}
		if self.punctuation_delay:
			for punctuation in punctuation_delay_factor:
				if word.endswith(punctuation):
					return delay_factor * punctuation_delay_factor[punctuation]
			else:
				return delay_factor
		else:
			return delay_factor

	def open_file(self, file: str) -> str:
		if os.path.isfile(file):
			with open(file, 'r') as f:
				return f.read()
		else:
			print(f"file not found: '{file}'")
			exit()