""" open_file.py """
f1 = './file/test1.txt'
msg = 'Line 1\nLine 2\nLine Last'

# print(msg)

''' 
'''
# 以writable方式開啟一個文件
f1w = open(f1, 'w')

# 將msg寫到文件裡
f1w.write(msg)

# 關閉文件
f1w.close()

# 顯示文件內容
f1r = open(f1, 'r')
''' cont1 = f1r.read()

print('read()\n', cont1) 

cont2 = f1r.readline()
print('readline():\n', cont2)

cont3 = f1r.readlines()
print('readline():\n', cont3)
'''
