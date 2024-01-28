# MIDI Key Automator

Este script foi escrito em Python e gera arquivos '.MIDI' contendo sequências de notas do keyboard que foram feitas de forma configurada e programado pelo usuário, o output pode ser inserido em qualquer plugin que o input das notas será imposto na keyboard. Ele é projetado para criar sequencias e modulações para diversas aplicações em notas musicas, necessita o plugin para funcionamento.

## Pré-requisitos

- [Mido](https://github.com/mido/mido): Uma biblioteca Python para trabalhar com arquivos MIDI.

### BPM (Batidas Por Minuto)

Controle a velocidade da sequência ajustando o valor de `bpm` no código.

### Número de Compassos

Determine a extensão da sequência ajustando `num_compassos`.

### Notas Base

Especifique as notas iniciais da sequência configurando a lista `notas_base` no formato de números MIDI.

### Intervalo de Progressão

Ajuste o intervalo entre as notas na progressão utilizando `intervalo_progressao`.

### Saída

Os scripts gerarão um arquivo MIDI com a sequência de notas moduladas e o salvará como `output_modulado.mid`.

```bash
pip install mido

## Uso

```bash
python3 run_midi.py
python3 run_midi_v2test.py
