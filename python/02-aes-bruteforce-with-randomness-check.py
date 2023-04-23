from timeit import default_timer as timer
from binascii import b2a_hex

#- Config variables 
filename="test.adobe"
aes_key_size=32
min_distinct_bytes=10

#- Variables related to file processing
file_offset=0;
total_keys_found = 0;

start_time = timer()

try:
    #- Open the file
    with open(filename, 'rb') as f:

        #- Read till you find data
        while True:
            #- Seek to the new file offset
            f.seek(file_offset)

            #- Read the keysize number of bytes
            temp_key=f.read(aes_key_size)
            
            #- Exit condition 1: If the read buffer is less than keysize:
            if len(temp_key) < aes_key_size:
                break
            
            #- Exit condition 2: When there are no more bytes to be read from the file:
            if not temp_key:
                break
        

            #- Get the key 
            temp_key_str=b2a_hex(temp_key)

            #- Breaking down the key string into a list of bytes
            n=2
            temp_key_list=[temp_key_str[i:i+n] for i in range(0, len(temp_key_str), n)]
            #- Counting the distinct bytes in the key list
            distinct_bytes=len(set(temp_key_list))

            #- If the distinct bytes is more than what we desire, consider it as a potential key. 
            if distinct_bytes>=min_distinct_bytes:
                #- Print the key
                print(distinct_bytes)
                print(temp_key_str)
                #- Increment total number of keys found
                total_keys_found = total_keys_found +1

            #- Increment file offset one byte at a time
            file_offset=file_offset+1

except KeyboardInterrupt:
    print("User cancelled before end of file")

end_time = timer()
print("Total keys found: ", total_keys_found)
print("Time elapsed = ", end_time-start_time)
