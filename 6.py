f = open("./input/6.txt", "r")

stream = f.read()

def detect_marker(search_len, detect):
    for i in range(len(stream)):
        if i >= search_len:
            flag = True
            test_str = stream[i-search_len:i]
            for c in test_str:
                if test_str.count(c) > 1:
                    flag = False
                    break
            
            if flag:
                print(f"{detect}: {i}")
                break

detect_marker(4,'start-of-packet')
detect_marker(14,'start-of-message')