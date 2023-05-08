def fcfs(pages, capacity):
    page_fault=0
    frame=[]

    for page in pages:
        if page not in frame:
            if len(frame)<capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_fault+=1
    return page_fault

pages=[1,2,3,4,5,1,2,5,1,2,3,4,5]
capacity=3

page_fault=fcfs(pages, capacity)
print(page_fault)




























