import os
# will be needed later for m function
def multiply_chars(comm):
    char_index = 0
    while comm[char_index] != " ":
        char_index += 1
    num_input = comm[1:char_index]
    return comm[char_index+1:] * int(num_input)
        

# input loop
while True:
    try:
        command = input(">> ")
        req_func = command[0]
        remaining_command = command[2:]
        
        if req_func == "o":
            print(ord(remaining_command))
        if req_func == "a":
            print(chr(int(remaining_command)))
        if req_func == "m":
            print(multiply_chars(command))
        if req_func == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
    
    except IndexError:
        pass
    except KeyboardInterrupt:
        print("\nQuitting...")
        break
        
        