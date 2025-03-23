import re


def main():
    content = "- - item 1\n  - item 2"

    output_list = main_environment_simulator(content)
    
    print(''.join(output_list))


def main_environment_simulator(content, is_nesting_flag=False):
    output_list = []

    ul_open = False
    content_lines = content.splitlines()
    content_lines_len = len(content_lines)
    is_last_line = False

    for i, line in enumerate(content_lines):
        if i ==  content_lines_len - 1:
            is_last_line = True

        li_line, ul_open, is_nesting_flag = convert_list(line, ul_open, is_last_line, is_nesting_flag)
        output_list += li_line

        if not is_last_line:
            output_list.append('\n')
    
    return output_list


def convert_list(line, ul_open, is_last_line, is_nesting_flag):
    output = []
    list_pattern = r'(?:\s\s)*-\s(.*)'
    match = re.match(list_pattern, line)
    if match:
        match = match.group(1)
        # open ul if not already open
        if not ul_open:
            if is_nesting_flag:
                output.append('\n')

            output.extend(["<ul>", '\n'])
            ul_open = True

        line_text = main_environment_simulator(match, True)
        output.append("<li>")
        output += line_text
        output.extend(["</li>"])
    else:
        if ul_open:
            output.extend(["</ul>", '\n'])
            ul_open = False

        # Remove leading and trailing white spaces
        line = line.strip()
        output.append(line)

    if is_last_line and ul_open:
        output.extend(['\n', "</ul>"])
        if is_nesting_flag:
            output.append('\n')
        ul_open = False

    return output, ul_open, is_nesting_flag


if __name__ == "__main__":
    main()