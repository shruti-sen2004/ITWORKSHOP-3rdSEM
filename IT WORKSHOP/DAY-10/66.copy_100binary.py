input_file = input("ENTER THE NAME OF THE BINARY FILE: ")

with open(input_file, 'rb') as in_file:
    with open('output_file.dat', 'wb') as out_file:
        content = in_file.read(100)
        out_file.write(content)
                
        print(f"Successfully copied the first 100 characters from '{input_file}' to output_file.")