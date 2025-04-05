from markdown_light import Markdown

input_folder = './inputs'
output_folder = './outputs'

from pathlib import Path

files = [f for f in Path(input_folder).iterdir() if f.is_file()]

for i, input in enumerate(files):
    with open(input, 'r') as raw_file:
        content_md = raw_file.read()

    markdowner = Markdown()
    content_html = markdowner.to_html(content_md)


    with open(f"{output_folder}/{i}.html", 'w') as out_file:
        out_file.write(content_html)


# TODO: 
# ===Prepare all tests
# ===Try to create an html page with the output
# ===Recheck logic
# Place in wiki
# Try all the created pages
# Test editing and routes again
# Make video
# post

# debugging
# content_md = '* hi'
# markdowner = Markdown()
# content_html = markdowner.to_html(content_md)
# print(content_html)