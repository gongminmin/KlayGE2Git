if __name__ == "__main__":
	from mercurial import ui, hg
	repo = hg.repository(ui.ui(), "klayge-hg")
	user_set = set()
	total_revs = len(repo)
	for i in range(1, total_revs):
		print("Revision %d/%d" % (i, total_revs - 1))
		change_ctx = repo[i]
		user_set.add(change_ctx.user())

	usermap = open("SlimAuthorMap.txt", "w")
	for user in user_set:
		usermap.write("%s\n" % user)
	usermap.close()
