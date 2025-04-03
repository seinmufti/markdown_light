from markdown_light import Markdown

# input_file = './inputs/CSS.md'
# output_folder = './outputs'


# with open(input_file, 'r') as raw_file:
#     content_md = raw_file.read()
#     print(content_md)

# markdowner = Markdown()
# content_html = markdowner.to_html(content_md)


# with open(f"{output_folder}/test.md", 'w') as out_file:
#      out_file.write(content_html)


# TODO: 
# ===Prepare all tests
# ===Try to create an html page with the output
# ===Recheck logic
# Place in wiki
# Try all the created pages
# Test editing and routes again
# Make video
# post

content_md = '# hi\n\nthere'
markdowner = Markdown()
content_html = markdowner.to_html(content_md)
print(content_html)