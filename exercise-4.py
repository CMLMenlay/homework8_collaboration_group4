def chunking_by(numbers, chunck):
    ...
    # for i in range(0, len(numbers), chunck):
    #     yield numbers[i:i + chunck ]
    # final = list(chunking_by(numbers, chunck))
    # return final
# print (chunking_by([5, 4, 7, 3, 4, 5, 4], 3))

    if not chunking_by:
        return []
    
    return [numbers[i:i + chunck] for i in range(0, len(numbers), chunck)]

insert_list = [5, 4, 7, 3, 4, 5, 4]
insert_chunck = 3
result = chunking_by(insert_list, insert_chunck)
print (result)




