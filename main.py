from markdown_light import Markdown

markdowner = Markdown()
content = "- item 1\n- item 2\n- item 3"
to_html = markdowner.to_html(content)

# TODO: 
# ===Prepare all tests
# ===Try to create an html page with the output
# ===Recheck logic
# Place in wiki
# Try all the created pages
# Test editing and routes again
# Make video
# post

print(to_html)

with open('test.html', 'w') as html_file:
    html_file.write(to_html)