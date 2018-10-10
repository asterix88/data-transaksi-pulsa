# data transaksi isi ulang pulsa


import sys
import time
import os


if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")



def show_data():
	file = open("data_transaksi.txt","r")
	cn = file.read()
	print(cn)
	
	file.close()
	print("\n")
	
def insert_data():
	tanggal = input("Tanggal: ")
	nohp = input("No Handphone: ")
	nama = input("Atas nama: ")
	asli = input("harga asli: ")
	jual = input("harga jual: ")
	status = input("Status: ")
	
	file = open("data_transaksi.txt","a")
	file.write("Tanggal: "+tanggal+ "\n")
	file.write("Nomor HP: "+nohp+"\n")
	file.write("Nama: "+nama+ "\n")
	file.write("Harga Asli: "+asli+ "\n")
	file.write("Harga jual: "+jual+ "\n")
	file.write("Status Pembayaran: "+status+"\n")
	file.write("==========================")
	file.write("\n")
	
	file.close()
	time.sleep(1)
	print("\n")

def show_untung():
	with open("untung.txt") as file:
		lines = [line.strip() for line in file]
		print(lines)
		
	print("\n")
	
def insert_untung():
	untung_baru = input("Masukan keuntungan: ")
	file = open("untung.txt","a")
	
	file.write(untung_baru)
	file.write("\n")
	file.close()
	
	time.sleep(1)
	print("\n")
	
def menu():
	print("......... MENU .........")
	print("\n")
	print("[0] Show data transaksi")
	print("[1] Insert data transaksi")
	print("[2] Show data keuntungan")
	print("[3] Insert data keuntungan")
	print("[99] Exit")
	
	aa = input("menu…> ")
	if int(aa) == 0:
		show_data()
	elif int(aa) == 1:
		insert_data()
	elif int(aa) == 2:
		show_untung()
	elif int(aa) == 3:
		insert_untung()
	elif int(aa) == 99:
		print("Exiting...")
		time.sleep(1)
		sys.exit()
	else:
		print("an error occured")
		sys.exit()
	
		
if __name__ == "__main__":
	while(True):
		menu()