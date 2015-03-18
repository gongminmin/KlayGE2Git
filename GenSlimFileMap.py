if __name__ == "__main__":
	from mercurial import ui, hg
	repo = hg.repository(ui.ui(), "klayge-hg")
	exclude_folders = ("External/7z", "External/boost", "External/Cg", "External/DXSDK", "External/freetype", "External/libogg", "External/libvorbis", "External/OpenALSDK", "External/Python", "External/rapidxml", "External/wpftoolkit")
	exclude_files = ("glloader/doc/Doxyfile", "KlayGE/klayge_logo.ico", "KlayGE/Core/Src/KConfig/KConfig.rc", "KlayGE/Core/Src/KConfig/resource.h")
	exclude_exts = ("c", "cpp", "h", "hpp", "rc", "xml", "cmake", "txt", "Doxyfile", "fxml", "vcproj", "vcxproj", "filters", "project", "inl")
	exclude_file_set = set()
	total_revs = len(repo)
	for i in range(1, total_revs):
		print("Revision %d/%d" % (i, total_revs - 1))
		change_ctx = repo[i]
		for filename in change_ctx.files():
			ext = ""
			dot_place = filename.rfind(".")
			if (dot_place != -1):
				ext = filename[dot_place + 1:].lower()
							
			skip = False
			if filename in exclude_files:
				skip = True
			if ext in exclude_exts:
				skip = True
			for folder in exclude_folders:
				if (0 == filename.find(folder)):
					skip = True
					break

			if not skip:
				try:
					file_ctx = change_ctx[filename]
					
					if (file_ctx.isbinary()):
						exclude_file_set.add(filename)
					else:
						if (ext in ("dds", "png", "jpg", "bmp", "tga", "jdt", "meshml", "md5mesh", "md5anim", "7z", "kfx", "model_bin", "kmesh", "kmodel", "kfont", "ttf", "pfx", "avi", "dll", "exe", "so", "pdf")):
							exclude_file_set.add(filename)
				except:
					pass

	filemap = open("SlimFileMap.txt", "w")
	filemap.write('include .\n')
	filemap.write('include "External/7z/build"\n')
	filemap.write('include "External/7z/Patches"\n')
	filemap.write('include "External/boost/build"\n')
	filemap.write('include "External/boost/Patches"\n')
	filemap.write('include "External/Cg/build"\n')
	filemap.write('include "External/Cg/Patches"\n')
	filemap.write('include "External/DXSDK/build"\n')
	filemap.write('include "External/DXSDK/Patches"\n')
	filemap.write('include "External/freetype/build"\n')
	filemap.write('include "External/freetype/Patches"\n')
	filemap.write('include "External/libogg/build"\n')
	filemap.write('include "External/libogg/Patches"\n')
	filemap.write('include "External/libvorbis/build"\n')
	filemap.write('include "External/libvorbis/Patches"\n')
	filemap.write('include "External/OpenALSDK/build"\n')
	filemap.write('include "External/OpenALSDK/Patches"\n')
	filemap.write('include "External/Python/build"\n')
	filemap.write('include "External/Python/Patches"\n')
	filemap.write('include "External/rapidxml/build"\n')
	filemap.write('include "External/rapidxml/Patches"\n')
	filemap.write('include "External/wpftoolkit/build"\n')
	filemap.write('include "External/wpftoolkit/Patches"\n')
	filemap.write('\n')
	for folder in exclude_folders:
		filemap.write('exclude "%s"\n' % folder)
	exclude_files = list(exclude_file_set)
	exclude_files.sort()
	for filename in exclude_files:
		filemap.write('exclude "%s"\n' % filename)
	filemap.close()
