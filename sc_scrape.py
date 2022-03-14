import json

lines = []
with open('/Users/anish/Documents/anish/wordle/speaknow.txt') as f:
    lines = f.readlines()

title_list = []
url_list = []
count = 0
for line in lines:
    if('<a href' in line):
        count += 1
        line = line.replace("\"", "@")
        arr = line.split(" ")
        new_url_suffix = arr[3].split("?")[0].split("@")[1]
        #new_url_suffix = arr[5].split("?")[0].split("@")[1]
        new_url = "https://soundcloud.com" + new_url_suffix
        new_title = "Taylor Swift - " + line.split("@>")[1].split("<")[0]
        #print(f'line {count}: {new_url}; {new_title}')   
        title_list.append(new_title)
        url_list.append(new_url)
print(json.dumps(url_list, ensure_ascii=False))
print(json.dumps(title_list, ensure_ascii=False))