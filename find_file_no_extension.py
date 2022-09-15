
import os
import time
import fnmatch


def find_2(pattern, path):  # this will match a pattern
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result



file_name = '3364_pavl_0282 copy.*'
search_directory = '/Volumes/big4photo-2/My photo 2022'



start_time = time.time()


print(find_2(file_name, search_directory))




print("--- %s seconds ---" % (time.time() - start_time))