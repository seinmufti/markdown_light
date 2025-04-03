import re
from conversions import _convert_heading, _convert_strong, _convert_anchor, _convert_paragraph, _convert_list


class Markdown():
    def to_html(self, content):
        # Prepare input
        content_lines = content.splitlines()
        content_lines_len = len(content_lines)
        # Variable initializations
        content_html_list = []
        ul_open = False
        
        for i, line in enumerate(content_lines):
            # Boolean initialization
            match_found = False

            # Skip empty lines
            if re.fullmatch(r'\s*', line):
                continue

            if i ==  content_lines_len - 1:
                is_last_line = True
            else:
                is_last_line = False

            # Remove leading and traling white spaces, and commence conversion.
            line = line.strip()
            converted_line = line

            # Convert accessory elements
            converted_line = _convert_strong(converted_line)
            converted_line = _convert_anchor(converted_line)

            # Commence checking for li
            returned_li_conversion, li_matched, ul_open = _convert_list(converted_line, ul_open, is_last_line)
            if li_matched:
                match_found = True
                converted_line = returned_li_conversion
            else:
                # If li didnt match but ul still needs to be closed
                if ul_open:
                    content_html_list.append(returned_li_conversion)
                    ul_open = False

            if not match_found:
                # Commence checking for heading
                converted_line, heading_matched = _convert_heading(converted_line)
                if heading_matched:
                    match_found = True

            # If no matches were found, turn to paragraph.
            if not match_found:
                converted_line = _convert_paragraph(converted_line)

            content_html_list.append(converted_line)

            # If not last line, add newline
            if not is_last_line:
                content_html_list.append('\n')
        content_html_str = ''.join(content_html_list)

        return content_html_str