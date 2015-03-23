if __name__ == "__main__":
	from mercurial import ui, hg
	repo = hg.repository(ui.ui(), "klayge-slimmed-hg")
	rev_map = []
	total_revs = len(repo)
	for i in range(total_revs - 1, 0, -1):
		print("Revision %d/%d" % (i, total_revs - 1))
		change_ctx = repo[i]
		rev_map.append([i, change_ctx.extra().get("convert_revision", "")[0:12], "", int(change_ctx.date()[0]), change_ctx.description()])

	git_revs = []
	git_id_file = open("GitID.txt", "r")
	for line in git_id_file:
		git_revs.append((line[0:40], int(line[41:51]), line[52:len(line) - 1]))
	git_id_file.close()

	rev_map_file = open("SlimRevMap.txt", "w")
	for rev in rev_map:
		rev[4] = rev[4].replace("\n", " ")
		match_git_revs = []
		for git_rev in git_revs:
			if ((0 == rev[4].find(git_rev[2])) and (git_rev[1] == rev[3])):
				match_git_revs.append(git_rev)
		if 1 == len(match_git_revs):
			rev[2] = match_git_revs[0][0]
		else:
			rev[2] = "???@@@???"
		rev_map_file.write("%d %s %s %s\n" % (rev[0], rev[1], rev[2], rev[4]))
	rev_map_file.close()
