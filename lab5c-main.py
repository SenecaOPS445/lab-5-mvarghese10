import lab5c                

lab5c.add(10,5)             
15                          

lab5c.add('10',5)           
15                          

lab5c.add('10','5')         
15                          

lab5c.add('abc','5')                                                                                                                     
'error: could not add numbers'                                  

lab5c.add('hello','world')                                                                                                               
'error: could not add numbers'                                  

lab5c.read_file('seneca2.txt')
['Line 1\n', 'Line 2\n', 'Line 3\n']           

lab5c.read_file('file10000.txt')   
'error: could not read file'