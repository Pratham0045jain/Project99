import os
import shutil
import time

# main function
def main():

	# initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = "/PATH_TO_DELETE"

	# specify the days
	days = 30

	# converting days to seconds
	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# checking whether the file is present in path or not
	if os.path.exists(path):

		# iterating over each and every folder and file in the path
		for root_folder, folders, files in os.walk(path):

			# comparing the days with root_folder
			if seconds >= os.stat(root_folder).st_ctime:

				# removing the folder
				shutil.rmtree(root_folder)
				deleted_folders_count += 1 # incrementing count

				# breaking after removing the root_folder
				break

			else:

				# checking folder from the root_folder
				for folder in folders:

					# folder path
					folder_path = os.path.join(root_folder, folder)

					# comparing with the days
					if seconds >= os.stat(folder_path).st_ctime:

						# invoking the remove_folder function
						shutil.rmtree(folder_path)
						deleted_folders_count += 1 # incrementing count


				# checking the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the days
					if seconds >= os.stat(file_path).st_ctime:

						# invoking the remove_file function
						os.remove(file_path)
						deleted_files_count += 1 # incrementing count

		else:

			# if the path is not a directory
			# comparing with the days
			if seconds >= os.stat(path).st_ctime:

				# invoking the file
				os.remove(path)
				deleted_files_count += 1 # incrementing count

	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1 # incrementing count

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


if __name__ == '__main__':
	main()