import re
from content import content
from conversions import _convert_heading, _convert_strong, _convert_anchor, _convert_paragraph, _convert_list

class MarkDownerLight():
    def to_html(self, content):
        content_html = ""
        list_found = False
        heading_found = False
        len_lines = len(content)
        for i, line in enumerate(content):
            # If empty line, skip.
            if re.fullmatch(r'\s+', line):
                continue
            # Else, remove leading and traling white spaces, and commence conversion.
            line = line.strip()

            line, list_found = _convert_list(line)

            line, heading_found = _convert_heading(line)

            # Accessory elements
            line = _convert_strong(line)
            line = _convert_anchor(line)

            if not (heading_found or list_found):
                line = _convert_paragraph(line)

            content_html += line

            if i < len_lines - 1:
                content_html += '\n'

        return content_html
        

if __name__ == "__main__":
    markdowner = MarkDownerLight()
    markdowner.to_html(content)