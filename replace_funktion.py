def replace_str(string,pos,content):
    str_li=[]
    for letter in string:
         str_li.append(letter)
    str_li[pos]=str(content)
    ret_str=""
    for letter2 in str_li:
         ret_str+=letter2
    return ret_str