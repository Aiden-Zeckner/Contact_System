class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    def __init__(self,name,number): #basic initiation
        self.name=name
        self.number=number


    def __str__(self):#print format
        return f"{self.name}: {self.number}"
    
    

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def __init__(self,key,value): #node
        self.key=key
        self.value=value
        self.next=None



class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self,size):#initiation for size
        self.size=size
        self.data=[None]*size


    def hash_function(self,key):#aslso initiation for size
        total=0
        for char in key:
            total+=ord(char)
        return total % self.size


    def insert(self,key,value):#insert the data into hash
        index=self.hash_function(key)
        current=self.data[index]  
        if self.data[index] is None:#if reach none, add
            self.data[index]=Node(key,value)
            return
        while current: #loop until reach none
            if current.key==key: #failsafe foor duplicate
                current.value=value
                return
            if current.next is None: #end
                break  
            current=current.next       
        current.next=Node(key,value) #adds


    def search(self,key):#searches for data
        index=self.hash_function(key)
        current=self.data[index]
        while current:#looks for key
            if current.key==key:
                return current.value
            current=current.next
        return None
    

    def print_table(self):#printing of data
        for x, node in enumerate(self.data):
            if node is None:#if index point has None, then say it has no value
                print(f"Index {x}: Empty")
            else:
                print(f"Index {x}:", end=" ")
                current = node
                while current:
                    print(f"{current.value}", end=" -> " if current.next else "")#inserts data to end of the previous print
                    current = current.next
                print()

def Home():#home function
    table=HashTable(10)
    while True:
        answer=input("Would you like to 1. Add Contact 2. Search Contact 3. View Underlying hash table 4. Exit")
        if answer=="1":
            key=input("Name of Contact?")
            number=input("Number of Contact?")
            contact=Contact(key,number)
            table.insert(key,contact)
            print(f"Contact {key}: {number} added")
        elif answer=="2":
            key=input("Name of contact?")
            contact=table.search(key)
            if contact:
                print(contact)
            else:#failsafe if not found
                print("contact not found")
        elif answer=="3":
            table.print_table()
        elif answer=="4":
            print("Bye-Bye")
            break
        else:
            print("Not found. Type (1-4)")

#call
Home()