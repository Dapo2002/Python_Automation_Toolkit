#  Copies an entire folder and its content into a
#  Zip file whose filename increments.

import zipfile
import os


def backupToZip(folder):
    #  Backup the entire contents of a "folder" into a zipfile
    folder = os.path.abspath(folder)  # Make sure the folder is absolute

    #  Figure out the filename this code should use based on
    # what files already exists
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    #  Create the Zip File
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #  Walk the entire folder tree and compress the files in each folder.
    for folderName, subFolders, filenames in os.walk(folder):
        print(f'Adding files in {folderName}...')
        #  Add the current folder to the ZIP file.

        #  Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            filepath = os.path.join(folderName, filename)
            arcname = os.path.relpath(filepath, folder)
            backupZip.write(filepath, arcname)
    backupZip.close()
    print('Done!')


backupToZip('renameDates_testFolder')
