#get midi file and a table of midi instrument to MM instrument
#TODO:
#1. analyze the rhythm. split if the notes are too small to avoid errors.
#2. create CE templates for each of the rhythms.
import dataclasses
import enum
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
    "ID" : "end",
    "PixelArtID" : "b"
}
lengths = [(),(),()]
onenote_rslt = []
onenote_rslt.append(not_playing_CEtemplate.copy())
def get_rhythm_CEtemplate_list(start_frame: int, note_length_list: list[int], prefix: str):
    first_np = not_playing_CEtemplate.copy()
    first_np["ID"] = prefix + "np_pre"
    first_np["TransformConditionValue"] = start_frame
    first_np["TransformID"] = prefix + "p0"

    for i,note_length in enumerate(note_length_list):
        p = playing_CEtemplate.copy()
        p["ID"] = prefix + "p" + hex(i)[2:]
        p["TransformID"] = prefix + "np" + hex(i)[2:]

        np = not_playing_CEtemplate.copy()
        np["ID"] = prefix + "np" + hex(i)[2:]
        p["TransformID"] = prefix + "p" + hex(i)[2:]
print(onenote_rslt)