# vim: set fileencoding=utf-8 et sts=4 sw=4 :
# Part of phycolo, see LICENSE for details
# Copyright (C) 2013  Kai Blin <kai.blin@biotech.uni-tuebingen.de>

from phycolo.data import all_codons

def count_codons(record):
    '''Count the codons present in a record'''
    codons = {}
    for codon in all_codons:
        codons[codon] = 0

    for f in record.features:
        if f.type != 'CDS':
            continue
        sequence = str(f.extract(record.seq))
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            codons[codon] += 1

    return codons
