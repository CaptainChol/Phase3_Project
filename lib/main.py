import click
import random
from models import Converter, Encripted, Keys  
# from models import Keys
from cryptography.fernet import Fernet
from seed import session  

@click.command()
@click.option(
    "--choice",
    prompt="Enter your choice:\n1 for Enter Data You want to Encrypted\n2 for Genarating Keys\n3 for File Encrption  \n4 for File Decryption\n5 for View Keys \n6 for Delete Keys\n7 for View Encryptions \n8 for Delete Encryptions\n9 to Quit\n",
    type=click.IntRange(1, 9),
)
def menu(choice):
    if choice == 1:
        create_key(session)
    elif choice == 2:
        generate_keys(session)       
    elif choice == 3:
         file_encryption(session)        
    elif choice == 4:
        file_decryption(session)  
    elif choice == 5:
         view_list(session)        
    elif choice == 6:
        delete_key(session)  
    elif choice == 7:
        view_encryptions(session)        
    elif choice == 8:
        delete_encryptions(session)        
    elif choice == 9:
        print("Leaving..... Goodbye")

def generate_keys(session):      

    keys_list = []

    for _ in range(50):
        key_value = Fernet.generate_key()
       
        key_instance = Keys(keys=key_value.decode()) 
        session.add(key_instance)
       
        session.commit()
        keys_list.append(key_value)
        if key_instance:
            print("Keys generated successfully")
        else:
            print("no key genarated")    
        
    

def create_key(session):
    print("File you want to decrypt....")
    sentence = click.prompt("Enter your sentence")

    file = Converter(
        sentence=sentence
    )
    session.add(file)
    session.commit()

def file_encryption(session):
    print("File you want to Encrypt....")
    encrptys  = []
    keys_to_use = session.query(Keys).all()
    for key in  keys_to_use:
        key = key.keys
        f = Fernet(key)
        id = click.prompt("Enter the ID")
        chess = session.query(Converter).filter(Converter.id == id).first()
        if chess:
            encrypted_data = f.encrypt(chess.sentence.encode())
            print("The encrypted data is:", encrypted_data)
            file = Encripted(
                encript=encrypted_data,
                key=key
            )
            session.add(file)
            session.commit()
            print("Added Successfully")
            encrptys.append(encrypted_data)  
            
        else:
            print("No record found for the given ID.")
            
    
                

def file_decryption(session):
    print("File you want to decrypt....")
    
    id = click.prompt("Enter the ID")
    chess = session.query(Encripted).filter(Encripted.id == id).first()
    f = Fernet(chess.key)
    if chess:
        try:
            decrypted_data = f.decrypt(chess.encript)
            print("The decrypted data is:", decrypted_data.decode())
        except Exception as e:
            print("Decryption failed. Error:", str(e))
    else:
        print("No record found for the given ID.")
        
        
        
def view_list(session):
        print("View all the keys....")
        views = []
        key = session.query(Keys).all()
        for i in  key:
            print(i.keys) 
            print('*' * 50)
            views.append(i)
            
            
            
def delete_key(session):
            print("Deleting Keys.....") 
            id = click.prompt("Enter ID for Key you want to delete....")
            key = session.query(Keys).filter(Keys.id==id).first() 
            if key:
                session.delete(key)
                session.commit()
                print("Deleted successfully")
            else:
                print("No records for ID provided")    
                
def view_encryptions(session):
    print("Viewing Encryptions....")
    all = session.query(Encripted).all()
    for i in all:
        print(i.encript) 
        print(i.key)  
        print("*" * 20)             
 
def delete_encryptions(session):
    print("Deleting Encrptions....." )
    id = click.prompt("Enter ID for Encypts you want to delete....")
    encrypt_id = session.query(Encripted).filter(Encripted.id == id).first()
    if encrypt_id:
        session.delete(encrypt_id)
        session.commit()
        print("Deleted Successfully")
    else:
        print("no records found")    
                     
            

if __name__ == "__main__":
    menu()
