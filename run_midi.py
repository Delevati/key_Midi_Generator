from mido import MidiFile, MidiTrack, Message, MetaMessage


def calculate_microseconds_per_beat(bpm):
    return int(60 / bpm * 10**6)


def create_bassline_sequence(num_compassos, notas_base, intervalo_progressao):
    bassline = []
    for compasso in range(num_compassos):
        for index, note in enumerate(notas_base):
            # Ajustar a variação de notas para permanecer dentro do intervalo % BPM
            new_note = (note + index * intervalo_progressao + compasso) % 128
            bassline.append(new_note)
    return bassline

    #hiperparametro
def create_midi_file(output_file, bpm, bassline_sequence):
    ticks_per_beat = 480

    #tempo
    microseconds_per_beat = calculate_microseconds_per_beat(bpm)

    #call save
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    track.append(MetaMessage('time_signature',
                 numerator=4, denominator=4, time=0))
    track.append(MetaMessage('set_tempo', tempo=microseconds_per_beat, time=0))

    #input save key
    for index, note in enumerate(bassline_sequence):
        time = ticks_per_beat // 2 if index % 2 == 0 else ticks_per_beat // 4
        velocity = 64 + index * 10

        note = max(0, min(127, note))
        velocity = max(0, min(127, velocity))

        track.append(Message('note_on', note=note,
                     velocity=velocity, time=time))
        track.append(Message('note_off', note=note,
                     velocity=velocity, time=time))

    midi.save(output_file)

# Configurações básicas
bpm = 128
num_compassos = 8
output_file = 'output_modulado.mid'

# Notas base (no formato de números MIDI)
notas_base = [36, 48, 60, 72]

intervalo_progressao = 2

bassline_sequence = create_bassline_sequence(
    num_compassos, notas_base, intervalo_progressao)

create_midi_file(output_file, bpm, bassline_sequence)
