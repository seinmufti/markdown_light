import pytest
from markdown_light import Markdown


def test_heading():
    markdowner = Markdown()

    content = ["# hi", "####### hi", "#hi", "# hi # bye"]
    content_html = ["<h1>hi</h1>", "<p>####### hi</p>", "<p>#hi</p>", "<h1>hi # bye</h1>"]
    for i, line in enumerate(content):
        assert markdowner.to_html(line) == content_html[i]


def test_strong():
    markdowner = Markdown()

    content = ["**lorem**", "**lorem*", "***lorem***", "**lorem** hi **ipsum**"]
    content_html = ["<p><strong>lorem</strong></p>", "<p>**lorem*</p>", "<p>*<strong>lorem</strong>*</p>", "<p><strong>lorem</strong> hi <strong>ipsum</strong></p>"]
    for i, line in enumerate(content):
        assert markdowner.to_html(line) == content_html[i]


def test_anchor():
    markdowner = Markdown()

    content = ["[foo](www.bar.com)"]
    content_html = ['<p><a href="www.bar.com">foo</a></p>']
    for i, line in enumerate(content):
        assert markdowner.to_html(line) == content_html[i]


def test_list():
    markdowner = Markdown()
    # Testing one bulleted item
    content = "- item 1"
    output = "" \
    "<ul>\n" \
    "<li>item 1</li>\n" \
    "</ul>"

    html_output = markdowner.to_html(content)
    assert html_output == output


    # Testing two bulleted items
    content = "- item 1\n- item 2"
    output = "" \
    "<ul>\n" \
    "<li>item 1</li>\n" \
    "<li>item 2</li>\n" \
    "</ul>"

    html_output = markdowner.to_html(content)
    assert html_output == output


    # If first is ul, and last item is unmatched
    content = "- item 1\nitem 2"
    output = "" \
    "<ul>\n" \
    "<li>item 1</li>\n" \
    "</ul>\n" \
    "<p>item 2</p>"

    html_output = markdowner.to_html(content)
    assert html_output == output


    # Unconverted line sandwiched between two converted "li"s with seperate "ul"s
    content = "- item 1\nitem 2\n- item 3"
    output = "" \
    "<ul>\n" \
    "<li>item 1</li>\n" \
    "</ul>\n" \
    "<p>item 2</p>\n" \
    "<ul>\n" \
    "<li>item 3</li>\n" \
    "</ul>"

    html_output = markdowner.to_html(content)
    assert html_output == output

    
    # asterisk alternative
    content = "* item 1\n* item 2"
    output = "" \
    "<ul>\n" \
    "<li>item 1</li>\n" \
    "<li>item 2</li>\n" \
    "</ul>"

    html_output = markdowner.to_html(content)
    assert html_output == output


def test_hybrids():
    markdowner = Markdown()
    # Heading and strong
    content = "# **item 1**"
    output = "<h1><strong>item 1</strong></h1>"

    html_output = markdowner.to_html(content)
    assert html_output == output


    # Heading and strong within list item
    content = "- # **item 1**"
    output = "" \
    "<ul>\n" \
    "<li><h1><strong>item 1</strong></h1></li>\n" \
    "</ul>"

    html_output = markdowner.to_html(content)
    assert html_output == output


    # Multiple conversions
    content = "" \
    "- ### item 1\n" \
    "**lorem**\n" \
    "- [item 2](www.item2.com)\n" \
    "- # **[item 3](www.item3.com)**"
    output = "" \
    '<ul>\n' \
    '<li><h3>item 1</h3></li>\n' \
    '</ul>\n' \
    '<p><strong>lorem</strong></p>\n' \
    '<ul>\n' \
    '<li><a href="www.item2.com">item 2</a></li>\n' \
    '<li><h1><strong><a href="www.item3.com">item 3</a></strong></h1></li>\n' \
    '</ul>'

    html_output = markdowner.to_html(content)
    assert html_output == output


def test_empty_space():
    markdowner = Markdown()
    content = "item 1\n\nitem 2"
    output = "" \
    "<p>item 1</p>\n" \
    "<p>item 2</p>"

    html_output = markdowner.to_html(content)
    assert html_output == output