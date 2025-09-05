import os 

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"file name {filename}: Created succesfully")
    except FileExistsError:
        print(f"file name {filename}: already exist!")
    except Exception as E:
        print('an error occurred!')

def view_all_files():
    files = os.listdir()
    if not files:
        print('file not found')
    else:
        print('files in directory')
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} have been deleted succesfully')
    except FileNotFoundError:
        print('file not found')
    except Exception as E:
        print('an error occurred')

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as E:
        print('an error occurred')

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter data to add = ')
            f.write(content + "\n")
            print(f'content added to {filename} successfully')
    except Exception as E:
        print('an error occurred')

def main():
    while True:
        print('file Management App')
        print('1:create a file')
        print('2:view all file')
        print('3:delete file')
        print('4:read file')
        print('5:edit file')
        print('6:exist')

        choice = input('Enter your choise (1-6)= ')

        if choice == '1':
            filename = input("Enter the file name to create = ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input('enter the file name of file you want = ')
            delete_file(filename)
        elif choice == '4':
            filename = input('enter file name to read = ')
            read_file(filename)
        elif choice == '5':
            filename = input('edit the file you want = ')
            edit_file(filename)
        elif choice == '6':
            print("closing the application.....")
            break
        else:
            print('invalid syntax')

if __name__ == "__main__":
    main()
