import datetime
szoveg = input("<szöveg>: ")
ido = datetime.datetime.now()
modoltido = ido.strftime("%y/%m/%d %H:%M:%S")
file = open("Python/09.15/naplo.txt", "a", encoding="utf-8")
file.write(f"{modoltido} {szoveg} \n")
file.close()