import os
from xml.etree.ElementTree import parse

if __name__ == '__main__':
    path = "C:/work/film"
    dcp_tools = 'C:/work/dcptools/dcpTool.exe'
    for file in os.listdir(path):
        old_dcp_path = path + '/' + file
        xml_path = path + '/' + file.replace('dcp', 'xml')
        new_dcp_path = path + '/' + file.replace('5300', '5500')
        os.system(dcp_tools + ' -d "' + old_dcp_path + '" "' + xml_path + '"')
        doc = parse(xml_path)
        root = doc.getroot()
        root.find('UniqueCameraModelRestriction').text = 'Nikon D5500'
        doc.write(xml_path, xml_declaration=True)
        os.system(dcp_tools + ' -c "' + xml_path + '" "' + new_dcp_path + '"')
        os.remove(xml_path)
        os.remove(old_dcp_path)
