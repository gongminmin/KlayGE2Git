if __name__ == "__main__":
	import csv
	import re
	csv_file = open("ticket_change.csv", "rb")
	ticket_change = csv.reader(csv_file, delimiter=";")
	hg_hex_set = set()
	for row in ticket_change:
		if ("comment" == row[3]):
			words = re.findall(r"[\w']+", row[5])
			for word in words:
				if (12 == len(word)):
					hg_hex = True
					for ch in word:
						if (ch not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')):
							hg_hex = False
							break
					if hg_hex:
						hg_hex_set.add(word)
	csv_file.close()

	rev_mapping = {}
	rev_map_file = open("SlimRevMap.txt", "r")
	for line in rev_map_file:
		rev_mapping[line[5:17]] = line[18:58]
	rev_map_file.close()

	update_file = open("UpdateTicketChange.sql", "w")
	missing_file = open("MissingChangeset.txt", "w")
	for hg_hex in hg_hex_set:
		if (rev_mapping.get(hg_hex) != None):
			update_file.write("UPDATE ticket_change\n")
			update_file.write("SET newvalue = REPLACE(newvalue, '%s', '%s')\n" % (hg_hex, rev_mapping[hg_hex]))
			update_file.write("WHERE newvalue LIKE '%%%s%%';\n\n" % hg_hex)
		else:
			missing_file.write("%s\n" % hg_hex);
	update_file.close()
