#get midi file and a table of midi instrument to MM instrument
#TODO:
#1. analyze the rhythm. split if the notes are too small to avoid errors.
#2. create CE templates for each of the rhythms.
import dataclasses
import enum
import json
#notecontraption: the contraption that plays the same note multiple times
@dataclasses.dataclass(slots = True)
class MM_notecontraption:
    note: int
    instrument: int
    rhythm: list[int]
@dataclasses.dataclass(slots = True)
class Song:
    pass
#with open("music.mid") as input_midi_file:
#    pass
PLAYING_CE_DURATION = 7 #frames
not_playing_CEtemplate = {
    "Behavior" : 0,
    "CanPlayerStandOn" : True,
    "HitBoxHeight" : 16,
    "HitBoxWidth" : 48,
    "ID" : None,
    "PixelArtID" : "0",
    "TransformCondition" : 2,
    "TransformConditionValue" : 18,
    "TransformDelay" : 0,
    "TransformID" : None
}
playing_CEtemplate = {
    "Behavior" : 0,
    "CanPlayerStandOn" : True,
    "HitBoxHeight" : 16,
    "HitBoxWidth" : 16,
    "ID" : None,
    "PixelArtID" : "1",
    "TransformCondition" : 2,
    "TransformConditionValue" : PLAYING_CE_DURATION,
    "TransformDelay" : 0,
    "TransformID" : None
}
end_CEtemplate = {
    "Behavior" : 0,
    "CanHurtPlayer" : False,
    "CanInteractWithEnemies" : True,
    "CanPlayerStandOn" : True,
    "HitBoxHeight" : 16,
    "HitBoxWidth" : 48,
    "ID" : "end",
    "PixelArtID" : "0"
}
lengths = [(),(),()]
onenote_rslt = [end_CEtemplate.copy()]

def get_normalized_note_length_list(note_length_list: list[int]):
    pass
def get_rhythm_CEtemplate_list(start_frame: int, note_length_list: list[int], prefix: str):
    result = []
    first_np = not_playing_CEtemplate.copy()
    first_np["ID"] = prefix + "np_pre"
    first_np["TransformConditionValue"] = start_frame
    first_np["TransformID"] = prefix + "p0"
    result.append(first_np)

    for i,note_length in enumerate(note_length_list):
        p = playing_CEtemplate.copy()
        p["ID"] = prefix + "p" + hex(i)[2:]
        if i == len(note_length_list)-1: p["TransformID"] = "end"
        else: p["TransformID"] = prefix + "np" + hex(i)[2:]
        result.append(p)
        if i == len(note_length_list)-1: break
        np = not_playing_CEtemplate.copy()
        np["ID"] = prefix + "np" + hex(i)[2:]
        np["TransformID"] = prefix + "p" + hex(i+1)[2:]
        assert note_length-PLAYING_CE_DURATION>0
        np["TransformConditionValue"] = note_length-PLAYING_CE_DURATION
        result.append(np)
    return result
with open("MM_noteblock/result.json","w") as result_file:
    onenote_rslt.extend(get_rhythm_CEtemplate_list(20,[60,60,60,60,60,60],""))
    json.dump(onenote_rslt,result_file,indent=4)
#man I just want to play Bad Apple but I have to code