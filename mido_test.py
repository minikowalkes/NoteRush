import mido as m

msg = m.Message("note_on", note=60) #dont know what this does
msg.type
msg.note
msg.bytes()
thing = m.get_output_names()

#msg.copy(channel 1=2)

port = m.open_output(thing[1])
port.send(msg)

with m.open_input() as inport:
    for msg in inport:
        print(msg)

mid = m.MidiFile("song.mid")
for msg in mid.play():
    port.send(msg)
