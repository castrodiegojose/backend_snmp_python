from save_Mariadb import *
from save_XML import *


def switch(case, info):
    if case == "db":
        save_mariadb(info)               
    elif case == "file":
        create_file_ifnot_exis(info)
    elif case == "both":
        check_xml = check_info_xml(info)
        check_mariadb = check_info_mariadb(info)
        if check_xml or check_mariadb:
            print("Error: Ya existe el modelo")
        else:
            save_mariadb(info)
            create_file_ifnot_exis(info)
            