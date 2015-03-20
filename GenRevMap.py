if __name__ == "__main__":
	from mercurial import ui, hg
	repo = hg.repository(ui.ui(), "klayge-slimmed-hg")
	rev_map = []
	total_revs = len(repo)
	for i in range(1, total_revs):
		print("Revision %d/%d" % (i, total_revs - 1))
		change_ctx = repo[i]
		rev_map.append((i, change_ctx.hex(), change_ctx.extra().get("convert_revision", "")))

	rev_map_file = open("SlimRevMap.txt", "w")
	for rev in rev_map:
		rev_map_file.write("%d %s %s\n" % rev)
	rev_map_file.close()
