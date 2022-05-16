import xml.etree.ElementTree as ET
import os
from xml.etree.ElementTree import Element, tostring, parse, SubElement,XML


file_path = "../file/models.xml"
path = "../file"


def check_info_xml(info):
    result = os.stat(file_path).st_size
    if result != 0:
        doc_xml = parse(file_path)        
        root = doc_xml.getroot()
        counter=0
        for child in root:
            if child.find("vendor").text == str(info[0]):
                counter+=1
            if child.find("model").text == str(info[2]):
                counter+=1
            if child.find("software").text == str(info[1]):
                counter+=1      
        if counter == 3:
            return True
        else:
            return False
    else:
        return False


def add_info_xml(info):
    check = check_info_xml(info)
    if check:
        print("Ya existe el modelo en XML")
    else:
        print("Creando el model en XML")
        doc_xml = parse(file_path)
        root = doc_xml.getroot()
        newModel = Element("cm_model")
        ET.SubElement(newModel, "vendor").text = str(info[0])
        ET.SubElement(newModel, "model").text = str(info[2])
        ET.SubElement(newModel, "software").text = str(info[1])
        root.append(newModel)
        doc_xml.write(file_path, encoding="utf-8", xml_declaration=True)


def create_file_ifnot_exis(info):    
    # CHEQUEO SI EL file XML EXISTE
    if os.path.isfile(file_path):
        result = os.stat(file_path).st_size
        if result == 0:
            print("el file esta vacio")
            models = ET.Element("cm_models")
            model = ET.SubElement(models, "cm_model")
            ET.SubElement(model, "vendor").text = str(info[0])
            ET.SubElement(model, "model").text = str(info[2])
            ET.SubElement(model, "software").text = str(info[1])
            file = ET.ElementTree(models)
            file.write(file_path, xml_declaration=True, encoding="utf-8")
        else:
            add_info_xml(info)
    else:
        print("el xml no existe, creando file...")    
        models = ET.Element("cm_models")
        model = ET.SubElement(models, "cm_model")
        ET.SubElement(model, "vendor").text = str(info[0])
        ET.SubElement(model, "model").text = str(info[2])
        ET.SubElement(model, "software").text = str(info[1])
        file = ET.ElementTree(models)
        file.write(path + "\\models.xml", xml_declaration=True, encoding="utf-8")
