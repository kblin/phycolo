# vim: set fileencoding=utf-8 et sts=4 sw=4 :
# Part of phycolo, see LICENSE for details
# Copyright (C) 2013  Kai Blin <kai.blin@biotech.uni-tuebingen.de>

from collections import defaultdict

def count_codons(record):
    '''Count the codons present in a record'''
    codons = defaultdict(lambda: 0)
    all_codons = 0

    for f in record.features:
        sequence = str(f.extract(record.seq))
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            codons[codon] += 1
            all_codons += 1

    return codons, all_codons


def calculate_percentages(codons, count):
    '''Calculate the relative occurance of codons in percent'''
    keys = codons.keys()
    percentages = defaultdict(lambda: 0.0)
    for k in keys:
        percentages["%s_percent" % k] = float(codons[k])/count * 100

    return percentages

