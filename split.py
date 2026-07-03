import typing

'''
problem: the inputs are l, min_distance
the assign_note_layers will assign a layer value to every note
'''
'''
ex)
[1,2,3,10], d=4 -> [0,1,2,0]:

'''
def assign_note_layers(note_times: list[int],min_distance: int) -> tuple[int, list[int]]:
    note_times=note_times.copy()
    note_times.sort()
    print(note_times)

    note_layers: list[int] = [None for i in range(len(note_times))]
    last_note_times: list[int] = []

    for i,curr_note_time in enumerate(note_times):
        if i==0:
            note_layers[i]=0
            last_note_times.append(curr_note_time)
            continue
        min_note_layer=None
        for j,last_note_time in enumerate(last_note_times):
            if curr_note_time-last_note_time>=min_distance:
                if min_note_layer is None \
                    or last_note_time<last_note_times[min_note_layer]: min_note_layer=j
        if min_note_layer is None:
            note_layers[i]=len(last_note_times)
            last_note_times.append(curr_note_time)
        else:
            note_layers[i]=min_note_layer
            last_note_times[min_note_layer]=curr_note_time


    return (len(last_note_times),note_layers)
def split_notes_to_lists(note_times: list[int],min_distance: int):
    note_layers_output = assign_note_layers(note_times,min_distance)
    result:list[list[int]] = [[] for i in range(note_layers_output[0])]
    for curr_note_time,curr_note_layer in zip(note_times,note_layers_output[1],strict=True):
        result[curr_note_layer].append(curr_note_time)
    return result
def test_distance(l: list[int],min_distance: int):
    l=l.copy()
    l.sort()
    
    for i,curr_note_time in enumerate(l):
        if i==len(l)-1: break
        if l[i+1]-curr_note_time<min_distance:
            return (False, i, curr_note_time, l[i+1])
    return (True,)
test_list = []

print(assign_note_layers([1,2,3,4,5,6],3))
if __name__=='__main__':
    while True:
        input_us = input('notes: ').split(',')
        input_s = [int(i) for i in input_us]
        input_s.sort()
        min_distance = int(input('min_distance: '))
        print(split_notes_to_lists(input_s,min_distance))