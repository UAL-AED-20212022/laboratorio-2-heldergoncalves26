from controller import controller
from models import Node
from models import LinkedList

def main():
    linked_list = LinkedList()

    
    while True:
        comandos = input().split(" ")
        if comandos[0] == "RPI":
            RPI(linked_list, comandos[1])

        elif comandos[0] == "RPF":
            RPF(linked_list, comandos[1])

        elif comandos[0] == "RPDE":
            RPDE(linked_list, comandos[2], comandos[1])

        elif comandos[0] == "RPAE":
            RPAE(linked_list, comandos[2], comandos[1])

        elif comandos[0] == "RPII":
            RPII(linked_list,int(comandos[2]),comandos[1])

        elif comandos[0] == "VNE":
            VNE(linked_list)

        elif comandos[0] == "VP":
            VP(linked_list, comandos[1])

        elif comandos[0] == "EPE":
            EPE(linked_list)

        elif comandos[0] == "EUE":
            EUE(linked_list)

        elif comandos[0] == "EP":
            EP(linked_list, comandos[1])


def RPI(linked_list, country):
    controller.insert_at_start(linked_list, country)
    LinkedList.traverse_list(linked_list)

def RPF(linked_list, country):
    controller.insert_at_end(linked_list, country)
    LinkedList.traverse_list(linked_list)

def RPDE(linked_list, novo, country):
    controller.insert_after_country(linked_list, novo ,country)
    LinkedList.traverse_list(linked_list)

def RPAE (linked_list , novo, country):
    controller.insert_before_item(linked_list , novo, country)
    LinkedList.traverse_list(linked_list)
 
def RPII (linked_list, country,index):
    controller.insert_at_index(linked_list,country, index )
    LinkedList.traverse_list(linked_list)

def VNE(linked_list):
    count = controller.verify_count(linked_list)
    print(f"O número de elementos são {count}.")

def VP(linked_list, country):
    if controller.search_item(linked_list, country) == False:
       print(f"O país {country} não se encontra na lista.")
    else:
        print(f"O país {country} encontra-se na lista.")

def EPE(linked_list):
    controller.delete_at_start(linked_list)
    print(f"O primeiro país da lista foi eliminado com sucesso.")

def EUE(linked_list):
    controller.delete_at_end(linked_list)
    print(f"O ultimo país da lista foi eliminado com sucesso.")

def EP(linked_list,country):
    if controller.search_item(linked_list, country) == False:
       print(f"O país {country} não se encontra na lista.")
    
    else:
        controller.delete_country_by_value(linked_list,country)
        print(f"O país {country} foi eliminado com sucesso.")
