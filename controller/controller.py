from models.LinkedList import LinkedList

def insert_at_start(linked_list, country):
    return LinkedList.insert_at_start(linked_list, country)

def insert_at_end(linked_list, country):
    return LinkedList.insert_at_end(linked_list, country)    

def insert_after_country(linked_list , new, country):
    return LinkedList.insert_after_item(linked_list , new, country) 

def insert_before_item(linked_list , new, country):
    return LinkedList.insert_before_item(linked_list , new, country)

def insert_at_index(linked_list , country,index):
    return LinkedList.insert_at_index(linked_list,country,index)  

def verify_count(linked_list):
    return LinkedList.get_count(linked_list)

def search_item(linked_list, country):
    return LinkedList.search_item(linked_list, country)

def delete_at_start(linked_list):
    return LinkedList.delete_at_start(linked_list)

def delete_at_end(linked_list):
    return LinkedList.delete_at_end(linked_list)

def delete_country_by_value(linked_list, country):
    return LinkedList.delete_element_by_value(linked_list, country)