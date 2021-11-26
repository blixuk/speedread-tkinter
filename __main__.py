# file: speedread-terminal/__main__.py

from speedread import SpeedRead
from command import Command
cmd = Command(description="SpeedRead")

@cmd.command(
	cmd.argument("-f", "--file", help="file to read"),
	cmd.argument("-w", "--wpm", help="words per minute"),
	cmd.argument("-F", "--focus", action="store_true", help="use focus on word, highlighting center character"),
	cmd.argument("-d", "--delay", action="store_true", help="use word delay based on word length"),
	cmd.argument("-P", "--punctuation", action="store_true", help="use punctuation delay"),
	cmd.argument("-H", "--height", action="store_true", help="set display height"),
	cmd.argument("-W", "--width", action="store_true", help="set display width"),
	cmd.argument("-s", "--size", help="set font size")
)
def main(self, args):
	'''SpeedRead'''

	words_per_minute = 250
	word_focus = False
	word_delay = False
	punctuation_delay = False
	height = 100
	width = 500
	font_size = None

	if args.wpm:
		words_per_minute = args.wpm
	if args.focus:
		word_focus = args.focus
	if args.delay:
		word_delay = args.delay
	if args.punctuation:
		punctuation_delay = args.punctuation
	if args.height:
		height = args.height
	if args.width:
		width = args.width
	if args.size:
		font_size = args.size

	if args.file:
		SpeedRead(args.file, words_per_minute, word_focus, word_delay, punctuation_delay, height, width, font_size)
		
	else:
		print("No file specified")
		cmd.printHelp()

if __name__ == '__main__':
	cmd.parse()