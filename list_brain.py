import re


def main():
    content = "- - item 1\n  - item 2"

    output_list = main_environment_simulator(content)
    
    print(''.join(output_list))


def main_environment_simulator(content, nesting_flag=False):
    output_list = []

    ul_open = False
    content_lines = content.splitlines()
    content_lines_len = len(content_lines)
    last_line = False

    for i, line in enumerate(content_lines):
        if i ==  content_lines_len - 1:
            last_line = True

        li_line, ul_open, nesting_flag = convert_list(line, ul_open, last_line, nesting_flag)
        output_list += li_line
    
    return output_list


def convert_list(line, ul_open, last_line, nesting_flag):
    output = []
    list_pattern = r'-\s(.*)'
    match = re.match(list_pattern, line)
    if match:
        # open ul if not already open
        if not ul_open:
            if nesting_flag:
                output.append('\n')

            output.extend(["<ul>", '\n'])
            ul_open = True

        # line_text = match.group(1)
        line_text = main_environment_simulator(match.group(1), True)
        output.append("<li>")
        output += line_text
        output.extend(["</li>", '\n'])
    else:
        if ul_open:
            output.append("</ul>")
            ul_open = False

        # Remove leading and trailing white spaces
        line = line.strip()
        output.append(line)

    if last_line and ul_open:
        output.append("</ul>")
        if nesting_flag:
            output.append('\n')
        ul_open = False

    return output, ul_open, nesting_flag


if __name__ == "__main__":
    main()