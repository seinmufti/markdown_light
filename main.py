from markdown_light import MarkDownerLight
from content import content

markdowner = MarkDownerLight()
to_html = markdowner.to_html(content)

print(to_html)