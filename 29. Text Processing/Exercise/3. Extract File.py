given_input = input().split('\\')
file_and_extension = given_input[-1].split('.')
file = file_and_extension[0]
extension = file_and_extension[1]
print('File name:',file)
print('File extension:',extension)