#!/usr/bin/env python3
import argparse
import time
import platform
import random
import rtmidi


def send_midi_message(midi_out, status, note, velocity):
    midi_out.send_message([status, note, velocity])

    # hiperparametros
def play_modulated_bassline(midi_out):
    base_note = 36
    num_notes = 8

    bassline_notes = list(range(base_note, base_note + num_notes)) + \
        list(range(base_note + num_notes - 2, base_note - 1, -1))

    for note in bassline_notes:
        send_midi_message(midi_out, 0x90, note, 100)
        time.sleep(0.5)
        send_midi_message(midi_out, 0x80, note, 0)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--midi", type=str, default="MPD218 Port A",
                            help="Dispositivo MIDI de entrada (padrão: %(default)s).")
        args = parser.parse_args()

    midi_out = rtmidi.MidiOut()
    for idx, name in enumerate(midi_out.get_ports()):
        if args.midi in name:
            print("Dispositivo MIDI de saída encontrado: %s" % name)
            midi_out.open_port(idx)
            break
        else:
            print("Ignorando dispositivo MIDI não selecionado: ", name)

    if not midi_out.is_port_open():
        if platform.system() == 'Windows':
            print("As saídas MIDI virtuais não são suportadas no Windows.")
        else:
            print("Criando uma saída MIDI virtual.")
            midi_out.open_virtual_port(args.midi)

    if not midi_out.is_port_open():
        print("Nenhuma saída MIDI aberta, saindo.")
    else:
        print("Reproduzindo o bassline modulado.")
        play_modulated_bassline(midi_out)
