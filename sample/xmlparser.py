import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def parse_xml_file(filepath) -> Element:
    root_node: Element = ET.parse(filepath).getroot()
    return root_node


def validate_xml(filename: str, root: Element):
    """ Does a DOI exist """
    print('Start analysis for: ', filename)

    for tag in root.findall('ARTICLE/DOI'):
        if tag.text is None:
            print('-> DOI tag is empty')
