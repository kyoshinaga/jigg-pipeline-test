#!/usr/bin/python
import xml.etree.ElementTree as ET
import json

# To check two XML snippets are semantically equal, this method compares
# each element recursively.
# This methods are borrowed from:
# https://bitbucket.org/ianb/formencode/src/tip/formencode/doctest_xml_compare.py?fileviewer=file-view-default#cl-70
def xml_compare(x1, x2, reporter = False):
    if x1.tag != x2.tag:
        if reporter:
            print('Tags do not match: %s and %s' % (x1.tag, x2.tag))
        return False
    for name, value in x1.attrib.items():
        if x2.attrib.get(name) != value:
            if reporter:
                print('Attributes do not match: %s=%r, %s=%r' \
                        % (name, value, name, x2.attrib.get(name))))
            return False
    for name in x2.attrib.keys():
        if name not in x1.attrib:
            if reporter:
                print('x2 has an attribute x1 is mising: %s' \
                        % name)
            return False
    if not xml_text_compare(x1.text, x2.text):
        if reporter:
            print('text: r != %r' % (x1.text, x2.text))
        return False
    if not xml_text_compare(x1.tail, x2.tail):
        if reporter:
            print('tail: %r != %r' % (x1.tail, x2.tail))
        return False
    cl1 = x1.getchildren()
    cl2 = x2.getchildren()
    if len(cl1) != len(cl2):
        if reporter:
            print('children length differs, %i != %i' \
                    % (len(cl1), len(cl2)))
        return False
    i = 0
    for c1, c2 in zip(cl1, cl2):
        i += 1
        if not xml_compare(c1, c2, reporter=reporter):
            if reporter:
                print('children %i do not match: %s' \
                        % (i, c1.tag))
            return False
    return True

def xml_text_compare(t1, t2):
    if not t1 and not t2:
        return True
    if t1 == '*' or t2 == '*':
        return True
    return (t1 or '').strip() == (t2 or '').strip()

def json_comp(filename1, filename2):
    f1 = open(filename1)
    f2 = open(filename2)
    x1 = json.load(f1)
    x2 = json.load(f2)
    f1.close()
    f2.close()
    return json_ordered(x1) == json_ordered(x2)

def json_ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, json_ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(json_ordered(x) for x in obj)
    else:
        obj
