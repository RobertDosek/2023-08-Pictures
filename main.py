from PIL import Image

words = Image.open('word_matrix.png')
mask = Image.open("mask.png")

mask = mask.resize((1015, 559))
mask.putalpha(100)
words.paste(mask,(0,0),mask)
words.show()

