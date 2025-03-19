import re


def _convert_list(line):
    list_pattern = r'-\s(.*)'
    match = re.match(list_pattern, line)
    if match:
        # line_text = match.group(1)
        line_text = match.group(1)
        output = f"<ul>\n<li>{line_text}<li>\n<ul>"

        match_found = True
    else:
        output = line
        match_found = False

    return output, match_found


def _convert_heading(line, list_specification=False):
    heading_pattern  = r'(#{1,6})\s(.*)'
    match = re.match(heading_pattern, line)
    if match:
        len_symbol, line_text = len(match.group(1)), match.group(2)
        output = f"<h{len_symbol}>{line_text}</h{len_symbol}>"
        match_found = True
    else:
        output = line
        match_found = False

    if not list_specification:
        return output, match_found
    else:
        return output


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


def checker(pattern, line):
    match = re.search(pattern, line)
    if match:
        print(match.group(0))
    else:
        print("no match")