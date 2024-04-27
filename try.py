my_string = "::hwuiehf :; Hello."

punct_list = [".", ",", ":", ";", "!", "?", "-"]

for char in my_string:
    if char in punct_list:
        my_string = my_string.replace(char, "")
      
print(my_string)
