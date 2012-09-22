def main():
	money = int(raw_input("amount of money : "))
	sort = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
	bills = {10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0, 5:0, 1:0}
	for i in sort:
		#print "checking : %d" % i
		while money >= i:
			money -= i
			bills[i] += 1
	for k, v in sorted(bills.items()):
		print k, v

if __name__ == "__main__":
	while 1:
		main()