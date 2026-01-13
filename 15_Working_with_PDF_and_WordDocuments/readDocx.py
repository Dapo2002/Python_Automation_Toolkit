#!  python3

import collections.abc
collections.Sequence = collections.abc.Sequence
import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for paragraphs in doc.paragraphs:
        fullText.append('   ' + paragraphs.text)
    return '\n\n'.join(fullText)


print(getText('demo.docx'))
