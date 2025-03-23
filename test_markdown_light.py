import pytest
from markdown_light import MarkDownerLight


def test_heading():
    markdowner = MarkDownerLight()

    content = [["# hi"], ["####### hi"], ["#hi"], ["# hi # bye"]]
    content_html = ["<h1>hi</h1>", "<p>####### hi</p>", "<p>#hi</p>", "<h1>hi # bye</h1>"]
    for i, line in enumerate(content):
        assert markdowner.to_html(line) == content_html[i]


def test_strong():
    markdowner = MarkDownerLight()

    content = [["**lorem**"], ["**lorem*"], ["***lorem***"], ["**lorem** hi **ipsum**"]]
    content_html = ["<p><strong>lorem</strong></p>", "<p>**lorem*</p>", "<p>*<strong>lorem</strong>*</p>", "<p><strong>lorem</strong> hi <strong>ipsum</strong></p>"]
    for i, line in enumerate(content):
        assert markdowner.to_html(line) == content_html[i]


def test_anchor():
    markdowner = MarkDownerLight()

    content = [["[foo](www.bar.com)"]]
    content_html = ['<p><a href="www.bar.com">foo</a></p>']
    for i, line in enumerate(content):
        assert markdowner.to_html(line) == content_html[i]


def test_list():
    ...