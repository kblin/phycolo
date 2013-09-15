from unittest import TestCase

from os import path
from collections import defaultdict
from helperlibs.bio import seqio

from phycolo.actions import count_codons
from phycolo.actions import codon_table

_codon_table_template = '''Codon usage %(name)s:
TTT:\t%(TTT_count)s\t%(TTT)0.2f\t\tTCT:\t%(TCT_count)s\t%(TCT)0.2f\t\tTAT:\t%(TAT_count)s\t%(TAT)0.2f\t\tTGT:\t%(TGT_count)s\t%(TGT)0.2f
TTC:\t%(TTC_count)s\t%(TTC)0.2f\t\tTCC:\t%(TCC_count)s\t%(TCC)0.2f\t\tTAC:\t%(TAC_count)s\t%(TAC)0.2f\t\tTGC:\t%(TGC_count)s\t%(TGC)0.2f
TTA:\t%(TTA_count)s\t%(TTA)0.2f\t\tTCA:\t%(TCA_count)s\t%(TCA)0.2f\t\tTAA:\t%(TAA_count)s\t%(TAA)0.2f\t\tTGA:\t%(TGA_count)s\t%(TGA)0.2f
TTG:\t%(TTG_count)s\t%(TTG)0.2f\t\tTCG:\t%(TCG_count)s\t%(TCG)0.2f\t\tTAG:\t%(TAG_count)s\t%(TAG)0.2f\t\tTGG:\t%(TGG_count)s\t%(TGG)0.2f

CTT:\t%(CTT_count)s\t%(CTT)0.2f\t\tCCT:\t%(CCT_count)s\t%(CCT)0.2f\t\tCAT:\t%(CAT_count)s\t%(CAT)0.2f\t\tCGT:\t%(CGT_count)s\t%(CGT)0.2f
CTC:\t%(CTC_count)s\t%(CTC)0.2f\t\tCCC:\t%(CCC_count)s\t%(CCC)0.2f\t\tCAC:\t%(CAC_count)s\t%(CAC)0.2f\t\tCGC:\t%(CGC_count)s\t%(CGC)0.2f
CTA:\t%(CTA_count)s\t%(CTA)0.2f\t\tCCA:\t%(CCA_count)s\t%(CCA)0.2f\t\tCAA:\t%(CAA_count)s\t%(CAA)0.2f\t\tCGA:\t%(CGA_count)s\t%(CGA)0.2f
CTG:\t%(CTG_count)s\t%(CTG)0.2f\t\tCCG:\t%(CCG_count)s\t%(CCG)0.2f\t\tCAG:\t%(CAG_count)s\t%(CAG)0.2f\t\tCGG:\t%(CGG_count)s\t%(CGG)0.2f

ATT:\t%(ATT_count)s\t%(ATT)0.2f\t\tACT:\t%(ACT_count)s\t%(ACT)0.2f\t\tAAT:\t%(AAT_count)s\t%(AAT)0.2f\t\tAGT:\t%(AGT_count)s\t%(AGT)0.2f
ATC:\t%(ATC_count)s\t%(ATC)0.2f\t\tACC:\t%(ACC_count)s\t%(ACC)0.2f\t\tAAC:\t%(AAC_count)s\t%(AAC)0.2f\t\tAGC:\t%(AGC_count)s\t%(AGC)0.2f
ATA:\t%(ATA_count)s\t%(ATA)0.2f\t\tACA:\t%(ACA_count)s\t%(ACA)0.2f\t\tAAA:\t%(AAA_count)s\t%(AAA)0.2f\t\tAGA:\t%(AGA_count)s\t%(AGA)0.2f
ATG:\t%(ATG_count)s\t%(ATG)0.2f\t\tACG:\t%(ACG_count)s\t%(ACG)0.2f\t\tAAG:\t%(AAG_count)s\t%(AAG)0.2f\t\tAGG:\t%(AGG_count)s\t%(AGG)0.2f

GTT:\t%(GTT_count)s\t%(GTT)0.2f\t\tGCT:\t%(GCT_count)s\t%(GCT)0.2f\t\tGAT:\t%(GAT_count)s\t%(GAT)0.2f\t\tGGT:\t%(GGT_count)s\t%(GGT)0.2f
GTC:\t%(GTC_count)s\t%(GTC)0.2f\t\tGCC:\t%(GCC_count)s\t%(GCC)0.2f\t\tGAC:\t%(GAC_count)s\t%(GAC)0.2f\t\tGGC:\t%(GGC_count)s\t%(GGC)0.2f
GTA:\t%(GTA_count)s\t%(GTA)0.2f\t\tGCA:\t%(GCA_count)s\t%(GCA)0.2f\t\tGAA:\t%(GAA_count)s\t%(GAA)0.2f\t\tGGA:\t%(GGA_count)s\t%(GGA)0.2f
GTG:\t%(GTG_count)s\t%(GTG)0.2f\t\tGCG:\t%(GCG_count)s\t%(GCG)0.2f\t\tGAG:\t%(GAG_count)s\t%(GAG)0.2f\t\tGGG:\t%(GGG_count)s\t%(GGG)0.2f
'''

def get_file_path(name):
    '''Get the path of a test file'''
    dirname = path.dirname(__file__)
    return path.join(dirname, name)

class TestPhycoloActions(TestCase):
    '''Test the phycolo utility functions'''

    def setUp(self):
        self.record = seqio.read(get_file_path('melanin.gbk'))
        self.maxDiff = None

    def test_codon_table(self):
        '''Test actions.codon_table()'''
        exp_codons = defaultdict(lambda: 0)
        exp_codons['name'] = 'AB070938.1'
        counted = count_codons(self.record)
        total = 0
        for k in counted:
            exp_codons['{0}_count'.format(k)] = counted[k]
            total += counted[k]

        for k in counted:
            exp_codons[k] = float(counted[k]) / total * 100

        expected = _codon_table_template % exp_codons

        generated = codon_table(self.record)
        self.assertMultiLineEqual(expected, generated)
