import textwrap

def get_hex_list():
    hex_file = open("hex", "r").readlines()

    hex_lists = []

    for h in hex_file:
        hex_lists += h.strip().split(" ")
        
    final_hex_list = []
        
    for e in hex_lists:
        final_hex_list += textwrap.wrap(e, 2)
        
    used_hext_list = []

    for e in final_hex_list:
        if not e == "00":
            used_hext_list.append(hex(int(e, 16) << 4)[2:])
        if e == "c3":
            break
        
    return used_hext_list

xor_key = [0xc3, 0xba, 0xdb, 0x17, 0xc3, 0xba, 0xdb, 0x17]

hex_list = get_hex_list()

final_output = 0xa4cf9924a7a50fe9

hex_value = 0x0
for e in hex_list:
    hex_value += int(e, 16)
    
final_output -= hex_value
    
xored_output = textwrap.wrap(hex(final_output)[2:], 2)

password = ""

for i in range(len(xored_output)):
    output_value = int(xored_output[i], 16)
    password += chr(output_value ^ xor_key[i])
    
print(password[::-1])