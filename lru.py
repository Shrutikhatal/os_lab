def lru(pages, capacity):
    page_fault=0
    frame=[]
    recent=[]

    for page in pages:
        if page not in frame:
            if len(frame)<capacity:
                frame.append(page)
                recent.append(page)
            else:
                lru_page=recent.pop(0)
                frame.remove(lru_page)
                frame.append(page)
                recent.append(page)
            page_fault+=1
        else:
            recent.remove(page)
            recent.append(page)
    return page_fault

pages=[1,2,3,4,5,1,2,5,1,2,3,4,5,4,3,7,8]
capacity=3

page_fault=lru(pages, capacity)
print(page_fault)









#


















