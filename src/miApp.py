from operator import eq
from tkinter import SW
from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen
from switch import *
import sys 
import re


# VALIDACION DE LA IP DEL MODEM                 
def valid_ip(address): 
    parts = address.split(".") 
    if len(parts) != 4 or parts[3] == "": 
        return False         
    for item in parts: 
        if not 0 <= int(item) <= 255: 
            return False       
    return True


# UN POCO MAS SOFICTICADA PARA ORDENAR LA INFO 
def sort_info(info):
    info_equipment = []
    info_split = info.split(";")
    for i in info_split:
        search_vendor = re.search(r" VENDOR:", i)
        search_sw = re.search(r"SW_REV:", i)
        search_model = re.search(r" MODEL:", i)
        if search_vendor:
            index_vendor=info_split.index(i)
            vendor = info_split[index_vendor].split(": ")[1]
            info_equipment.append(vendor)
        if search_sw:
            index_sw=info_split.index(i)
            software = info_split[index_sw].split(": ")[1]
            info_equipment.append(software)
        if search_model:
            index_model=info_split.index(i)
            model = info_split[index_model].split(": ")[1][0:-3]
            info_equipment.append(model)
    return info_equipment


# response SNMPGET       
def get_snmp(ip_modem):     
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('private', mpModel=1),
        UdpTransportTarget((ip_modem, 161)),
        ContextData(),
        ObjectType(ObjectIdentity('.1.3.6.1.2.1.1.1.0'))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        print(errorIndication)
        return False
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        return False
    else:        
        variable = str(varBinds[0][1])
        return variable


# MAIN PROGRAM
if __name__ == "__main__":
    try:
        ip_modem = sys.argv[1]
        flag_db = sys.argv[2]
        # VALIDO IP
        validate =  valid_ip(ip_modem)
        if validate:
            print("La ip es valida")
            # REALIZO EL SNMP GET
            response = get_snmp(ip_modem)
            if response != False:
                # ORDENO LA INFORMACION
                info = sort_info(response)
                # ENVIO INFORMACION AL switch JUNTO CON EL METODO DE ALMACENAMIENTO
                switch(flag_db, info)
            else:
                print("No hay response")  
        else:
            print("Ingrese una IP Valida")
    except IndexError:
        print("Error: Faltan argumentos")
