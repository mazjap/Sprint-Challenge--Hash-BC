#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    length -= 1
    route = [None] * length
    destination = None
    for ticket in tickets:
        if ticket.source is "NONE":
            destination = ticket.destination
        else:
            hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    for index in range(length):
        route[index] = destination
        destination = hash_table_retrieve(hashtable, destination)
    return route
