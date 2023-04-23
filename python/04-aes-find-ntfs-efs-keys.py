import re

#- Name of the file/drive letter to scan
#input_file_name="C:\\memory.dmp"
input_file_name="test.adobe"
key_len=32


#- Open the input file
with open(input_file_name, "rb") as f:
    #- Signature to match "2000 0000 2000 0000 1066 0000 0000 0000" (bytes)
    #- Ref: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/00933615-c9cf-4d51-9d9a-bb3fb33a3560
    match_str=b'\x20\x00\x00\x00\x20\x00\x00\x00\x10\x66\x00\x00\x00\x00\x00\x00'

    #- Match regex on input file
    matches=re.finditer(match_str,f.read())
    
    #- List to store extracted records
    efs_key_recs=[]
    
    #- Iterate through the matches
    for m in matches:
        #print(m)
        #- Get the start offset
        start_offset=m.start()

        #- Seek to location of the Key
        f.seek(start_offset+16)
        
        #- Read the EFS key
        efs_key=f.read(key_len)
        
        #- Append key to output list
        efs_key_recs.append(efs_key)
        

    print("The following EFS keys were found: ")
    print(efs_key_recs)
