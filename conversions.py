import re


def _convert_list(content_html, line, root_ul_open):
    list_pattern = r'-\s(.*)'
    match = re.match(list_pattern, line)
    if match:
        li_matched = True

        # Open ul if ^li_matched and ul is not open
        if not root_ul_open:
            content_html.extend(["<ul>", "\n"]) 
            root_ul_open = True

        # Check the inside of li for other matches
        content_html.append(f"<li>{match.group(1)}</li>")
    else:
        li_matched = False

        # If li not matched, and ul is still open, close it.
        if root_ul_open:
            content_html.extend(["</ul>", "\n"])
            root_ul_open = False
        

    return li_matched, root_ul_open


def _convert_heading(line, nesting_flag=False):
    heading_pattern  = r'(#{1,6})\s(.*)'
    match = re.match(heading_pattern, line)
    if match:
        len_symbol, line_text = len(match.group(1)), match.group(2)
        output = f"<h{len_symbol}>{line_text}</h{len_symbol}>"
        match_found = True
    else:
        output = line
        match_found = False

    if not nesting_flag:
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


def initiation_wrapper(line, ul_open, li_matched, nesting_flag):
    line = _convert_list(line, ul_open, li_matched, nesting_flag)
    """
    # line = _convert_heading(line, nesting_flag)
    # line = _convert_strong(line)
    # line = _convert_anchor(line)
    """

    return line

