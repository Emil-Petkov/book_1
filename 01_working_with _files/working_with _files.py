# read text from file

test_file = open('C:\\Users\\...\\Desktop\\test.txt')
text = test_file.read()

print(text)

##################################

# new text

test_file = open('C:\\Users\\...\\Desktop\\test.txt', 'w')
new_content = input()
text = test_file.write(new_content)

test_file.close()

###################################
# auto close

with open('C:\\Users\\...\\Desktop\\test.txt', 'a') as test_file:
    add_new_text = input()
    test_file.write(add_new_text + '\r\n')

with open('C:\\Users\\...\\Desktop\\test.txt', 'r') as read_file:
    content = read_file.read()
    print(content)
