import re
from content import content
from conversions import _convert_heading, _convert_strong, _convert_anchor, _convert_paragraph, _convert_list

class MarkDownerLight():
    def to_html(self, content):
        content_html_list = []
        root_ul_open = False
        
        len_lines = len(content)
        for i, line in enumerate(content):
            # Bool initializations
            match_found = False
            li_matched = False

            # If empty line, skip.
            if re.fullmatch(r'\s+', line):
                continue
            # Else, remove leading and traling white spaces, and commence conversion.
            line = line.strip()

            # Commence checking for li
            line, li_matched, root_ul_open = _convert_list(line, root_ul_open)
            if li_matched:
                match_found = True

            """
            if not match_found:
                # Commence checking for heading
                line, heading_matched = _convert_heading(line)
                if heading_matched:
                    match_found = True

            # Accessory elements
            line = _convert_strong(line)
            line = _convert_anchor(line)
            
            """

            # If no matches were found, turn to paragraph.
            if not match_found:
                line = _convert_paragraph(line)

            content_html_list.append(line)
            
            # If reached the last line, and ul still open, close it.
            if root_ul_open and i == len_lines - 1:
                content_html_list.extend(['\n', "</ul>"])

            # If not last line, add newline
            if i < len_lines - 1:
                content_html_list.append('\n')

        return ''.join(content_html_list)
        

if __name__ == "__main__":
    markdowner = MarkDownerLight()
    html_content = markdowner.to_html(content)
    print(html_content)