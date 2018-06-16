import msvcrt
 
print("Press 'D' to exit...")
 
while True:
    if ord(msvcrt.getch()) in [68, 100]:
        break