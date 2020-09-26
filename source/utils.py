def return_index(movies, name):
    index = -1
    for i in range(len(movies)):
            if movies[i]['Title'] == name:
                index = i
                break
    return index
def ret_index(movies, id):
    index = -1
    for i in range(len(movies)):
            if movies[i]['id'] == id:
                index = i
                break
    return index