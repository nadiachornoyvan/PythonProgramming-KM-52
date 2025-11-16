dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]

def search_recursive(nodes, filename, current_path):
   
    found_paths = [] 
    
    for item in nodes:
        
        if isinstance(item, str):
            if item == filename:
                
                full_path = f"{current_path}/{item}"
                found_paths.append(full_path)
        
        elif isinstance(item, tuple):
            folder_name = item[0]
            subnodes = item[1]
            
            if current_path == "":
                new_path = f"/{folder_name}"
            else:
                new_path = f"{current_path}//{folder_name}"
            
            found_paths.extend(search_recursive(subnodes, filename, new_path))
            
    return found_paths

def search(dirs, filename):
  
    return search_recursive(dirs, filename, "")


print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))

assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')