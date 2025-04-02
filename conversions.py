import re


def _convert_list(line, ul_open, is_last_line):
    li_matched = False
    output = []

    li_pattern = r'-\s(.*)'
    match = re.match(li_pattern, line)
    if match:
        # Boolean for returning output opening and closing output seperately,
        # And indicating if li was found to not be converted to <p> later.
        li_matched = True

        match = match.group(1)
        # open ul if not already open
        if not ul_open:
            output.extend(["<ul>", '\n'])
            ul_open = True

        converted_line, _ = _convert_heading(match)

        output.extend(["<li>", converted_line, "</li>"])

        if is_last_line:
            # If last line, close the matched li with opened ul.
            output.extend(["\n", "</ul>"])
            ul_open = False
    else:
        # If not li, and ul is still open, close it.
        if ul_open:
            output.extend(["</ul>", '\n'])
        else:
            output.append(line)

    # Convert output to str
    output_str = ''.join(output)
                
    return output_str, li_matched, ul_open
    

def _convert_heading(line):
    match_found = False

    heading_pattern  = r'(#{1,6})\s(.*)'
    match = re.match(heading_pattern, line)
    if match:
        len_symbol, line_text = len(match.group(1)), match.group(2)
        line = f"<h{len_symbol}>{line_text}</h{len_symbol}>"
        match_found = True

    return line, match_found


def _convert_strong(line):
    strong_pattern = r'\*{2}([^*].*?)\*{2}'
    strong_html_pattern = r'<strong>\1</strong>'
    output = re.sub(strong_pattern, strong_html_pattern, line)
    return output


def _convert_anchor(line):
    anchor_pattern = r'\[(.*?)\]\((.*?)\)'
    anchor_html_pattern = r'<a href="\2">\1</a>'
    output = re.sub(anchor_pattern, anchor_html_pattern, line)
    return output


def _convert_paragraph(line):
    paragraph_html = f"<p>{line}</p>"
    return paragraph_html