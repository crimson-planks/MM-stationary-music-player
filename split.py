import typing

'''
problem: the inputs are l, min_distance
the assign_note_layers will assign a layer value to every note
'''
'''
ex)
[1,2,3,10], d=4 -> [0,1,2,0]:

'''
def assign_note_layers(l: list[int],min_distance: int):
    l=l.copy()
    l.sort()

    note_layers: list[None|int] = [None for i in range(len(l))]
    last_note_times: list[int] = []

    for i,curr_note_time in enumerate(l):
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
        min_distance = int(input('min_distance: '))
        print(assign_note_layers(input_s,min_distance))