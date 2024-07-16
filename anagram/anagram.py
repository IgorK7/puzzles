def find_anagrams(word, candidates):
    result = []
    for i in candidates:
        count1 = 0
        # print(i)
        candsp = list(i)
        # print(candsp)
        for j in word:
            # print(j)
            if j in candsp:
                candsp.remove(j)
                # print(candsp)
                count1 += 1
            else:
                #print("continue")
                break
        if len(i) == count1:
            result.append(i)
    return(result)
    
    
find_anagrams(word, candidates)