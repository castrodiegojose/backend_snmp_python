import conexion_mysql
from conexion_mysql import Customer
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=conexion_mysql.engine)
session = Session()


def save_mariadb(info):
    exist = check_info_mariadb(info)
    if exist:
        print("Ya existe el elemento en MariaDB")
    else:
        new_model = Customer(Model = info[2], Vendor = info[0], Softver = info[1])
        session.add(new_model)
        session.commit()    
        print("Guardando en MariaDB")


def check_info_mariadb(info):
    Session = sessionmaker(bind=conexion_mysql.engine)
    session = Session()
    models = session.query(Customer).all()
    counter = 0
    for model in models:
        if model.Model == info[2]:
            counter += 1
        if model.Vendor == info[0]:
            counter += 1
        if model.Softver == info[1]:
            counter += 1
    if counter == 3:
        return True
    else:
        return False
