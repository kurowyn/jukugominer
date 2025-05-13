import sys

HIRAGANA = ('あいうえおぁぃぅぇぉゔかきくけこさしすせそたちつてとっなにぬねのんはひふへほまみ' 
		   'むむめもやゆよゃゅょらりるれろわゐゑをがぎぐげござじじずぜぞだぢぢづでどばびぶべぼ'
		   'ぱぴぷぺぽぽーゝゞ、。')
KATAKANA = ('アイウエオァィゥェォォヴカキクケコサシスセソタチツツテトッナニヌネノンハヒフヘホマ' 
		   'ミムメモヤユヨャュョラリルレロワヰヱヲガギグゲゴザザジズゼゾダヂヅデドバビブベボパ' 
		   'ピプペポ・ーヽヾ、。ヴッン')
JP_NUMS = '１２３４５６７８９０'
NUMS = '1234567890'

def parse_jukugo(jp_lines):
	jukugo = jp_lines
	for letter in jp_lines:
		if letter in HIRAGANA + KATAKANA + JP_NUMS + NUMS:
			jukugo = jukugo.replace(letter, ' ', 1)
	jukugo = jukugo.split()
	return jukugo

# Basically, we need a function that finds Kanji Jukugo.	
# Jukugo are everything but:
# Hiragana
# Katakana
# JP-Punctuations
# EN-Punctuations
# JP-Nums 
# EN-Nums
# ...and so on.
			
if len(sys.argv) != 2:
	print('usage: python jukugo_finder {filename}')
	exit(1)

filename = sys.argv[1]

try:
	with open(filename, encoding = 'utf8') as f:
		lines = ''.join(f.readlines())
		jukugo = parse_jukugo(lines)
		with open('jukugo_file', encoding = 'utf8', mode = 'w') as jukugo_f:
			print(*jukugo, sep = '\n', end = '', file = jukugo_f)
except:
	print(f'ERR: no such file {filename}. Exiting.')
	exit(1)
