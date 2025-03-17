import re


def main():
    content = read_md("test.md")
    ul_exists = False
    content_html = ""
    len_lines = len(content)

    for i, line in enumerate(content):
        # If empty line, skip.
        if re.fullmatch(r'\s+', line):
            continue
        # Else, remove leading and traling white spaces, and commence conversion.
        line = line.strip()
        line = convert_strong(line)
        line = convert_anchor(line)
    
        # If heading
        heading = convert_heading(line)
        if heading:
            content_html += heading
            if i < len_lines - 1:
                content_html += '\n'
                # Reset ul to be created in the next li instance.
                ul_exists = False
            continue
    
        # If li
        li_pattern  = r'-\s?(.*)'
        li_matches = re.search(li_pattern, line)
        if li_matches:
            li = li_matches.group(1)
            if ul_exists:
                # Create the <li> without <ul> tags
                li_html = f"<li>{li}</li>"
                # Split according to backslashes
                content_html_split = (content_html.split('\n'))
                # Insert <li> into second to last position of contents
                content_html_split.insert(-2, li_html)
    
                # Rejoin split list into string
                content_html = '\n'.join(content_html_split)
            else:
                # Create the <li> with <ul> tags
                li_html = f"<ul>\n<li>{li}</li>\n</ul>"
                ul_exists = True
                content_html += li_html
                if i < len_lines - 1:
                    content_html += '\n'
            continue

        # If paragraph
        paragraph = convert_paragraph(line)
        content_html += paragraph
        if i < len_lines - 1:
            content_html += '\n'
            ul_exists = False
        
        
    write_html("test.html", content_html)


def convert_heading(line):
    heading_pattern  = r'(#+)\s?(.*)'
    heading_matches = re.fullmatch(heading_pattern, line)
    if heading_matches:
        heading_sym_matches = len(heading_matches.group(1))
        heading = heading_matches.group(2)

        heading_html = f"<h{heading_sym_matches}>{heading}</h{heading_sym_matches}>"
        return heading_html
    

def convert_paragraph(line):
    paragraph_html = f"<p>{line}</p>"
    return paragraph_html


def convert_li(line):
    ...


def read_md(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        return lines


def write_html(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)


def convert_strong(line):
    strong_pattern = r'\*{2}(.*?)\*{2}'
    strong_html_pattern = r'<strong>\1</strong>'
    line = re.sub(strong_pattern, strong_html_pattern, line)
    return line


def convert_anchor(line):
    anchor_pattern = r'\[(.*?)\]\((.*?)\)'
    anchor_html_pattern = r'<a href="\2">\1</a>'
    line = re.sub(anchor_pattern, anchor_html_pattern, line)
    return line


if __name__ == "__main__":
    main()