if __name__ == "__main__":
	from mercurial import ui, hg
	repo = hg.repository(ui.ui(), "klayge-hg")
	exclude_folders = ("External")
	exclude_files = ("glloader/doc/Doxyfile", "KlayGE/klayge_logo.ico")
	exclude_exts = ("c", "cpp", "h", "hpp", "rc", "xml", "cmake", "txt", "Doxyfile", "fxml")
	resource_file_set = set()
	change_ctx = repo[len(repo) - 1]
	for file_name in change_ctx:
		ext = ""
		dot_place = file_name.rfind(".")
		if (dot_place != -1):
			ext = file_name[dot_place + 1:].lower()

		skip = False
		if file_name in exclude_files:
			skip = True
		if ext in exclude_exts:
			skip = True
		for folder in exclude_folders:
			if (0 == file_name.find(folder)):
				skip = True
				break

		if not skip:
			try:
				file_ctx = change_ctx[file_name]
				
				if (file_ctx.isbinary()):
					resource_file_set.add(file_name)
				else:
					if (ext in ("dds", "png", "jpg", "bmp", "tga", "jdt", "meshml", "md5mesh", "md5anim", "7z", "kfx", "model_bin", "kmesh", "kmodel", "kfont", "ttf", "pfx", "avi", "dll", "exe", "so", "pdf")):
						resource_file_set.add(file_name)
					elif (file_ctx.size() > 32 * 1024):
						resource_file_set.add(file_name)
			except:
				pass

	for file_name in resource_file_set:
		print(file_name)
		slash_place = file_name.rfind("/")
		dir_name = "klayge-hg-resources/" + file_name[0:slash_place]
		import os
		try:
			os.makedirs(dir_name)
		except:
			pass
		import shutil
		shutil.move("klayge-hg/" + file_name, dir_name)
