def read_sample_file():
    """demonstrate basic file reading-----
    hvsiohiuvdn
    """
    file = open("sample.txt","r")
    # print(f"here is the file I wanted to read_______ : {file}")
    content = file.read()
    print(f"here is the content of the file read: {content}")
    file.close()
    return content

read_sample_file()