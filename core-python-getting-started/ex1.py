from urllib.request import urlopen

response = urlopen('http://sixty-north.com/c/t.txt')
story = []

for line in response:
    words = line.decode('utf-8').split()

    for word in words:
        story.append(word)

response.close()
print(story)