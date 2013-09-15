# vim: set fileencoding=utf-8 et sts=4 sw=4 :
# Part of phycolo, see LICENSE for details
# Copyright (C) 2013  Kai Blin <kai.blin@biotech.uni-tuebingen.de>

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from phycolo.data import all_codons

Base = declarative_base()
Session = sessionmaker()

class Fingerprint(Base):
    __tablename__ = 'fingerprint'
    name = Column(String(64), primary_key=True)
    total_count = Column(Integer)
    AAA_count = Column(Integer)
    AAC_count = Column(Integer)
    AAG_count = Column(Integer)
    AAT_count = Column(Integer)
    ACA_count = Column(Integer)
    ACC_count = Column(Integer)
    ACG_count = Column(Integer)
    ACT_count = Column(Integer)
    AGA_count = Column(Integer)
    AGC_count = Column(Integer)
    AGG_count = Column(Integer)
    AGT_count = Column(Integer)
    ATA_count = Column(Integer)
    ATC_count = Column(Integer)
    ATG_count = Column(Integer)
    ATT_count = Column(Integer)
    CAA_count = Column(Integer)
    CAC_count = Column(Integer)
    CAG_count = Column(Integer)
    CAT_count = Column(Integer)
    CCA_count = Column(Integer)
    CCC_count = Column(Integer)
    CCG_count = Column(Integer)
    CCT_count = Column(Integer)
    CGA_count = Column(Integer)
    CGC_count = Column(Integer)
    CGG_count = Column(Integer)
    CGT_count = Column(Integer)
    CTA_count = Column(Integer)
    CTC_count = Column(Integer)
    CTG_count = Column(Integer)
    CTT_count = Column(Integer)
    GAA_count = Column(Integer)
    GAC_count = Column(Integer)
    GAG_count = Column(Integer)
    GAT_count = Column(Integer)
    GCA_count = Column(Integer)
    GCC_count = Column(Integer)
    GCG_count = Column(Integer)
    GCT_count = Column(Integer)
    GGA_count = Column(Integer)
    GGC_count = Column(Integer)
    GGG_count = Column(Integer)
    GGT_count = Column(Integer)
    GTA_count = Column(Integer)
    GTC_count = Column(Integer)
    GTG_count = Column(Integer)
    GTT_count = Column(Integer)
    TAA_count = Column(Integer)
    TAC_count = Column(Integer)
    TAG_count = Column(Integer)
    TAT_count = Column(Integer)
    TCA_count = Column(Integer)
    TCC_count = Column(Integer)
    TCG_count = Column(Integer)
    TCT_count = Column(Integer)
    TGA_count = Column(Integer)
    TGC_count = Column(Integer)
    TGG_count = Column(Integer)
    TGT_count = Column(Integer)
    TTA_count = Column(Integer)
    TTC_count = Column(Integer)
    TTG_count = Column(Integer)
    TTT_count = Column(Integer)
    AAA = Column(Float)
    AAC = Column(Float)
    AAG = Column(Float)
    AAT = Column(Float)
    ACA = Column(Float)
    ACC = Column(Float)
    ACG = Column(Float)
    ACT = Column(Float)
    AGA = Column(Float)
    AGC = Column(Float)
    AGG = Column(Float)
    AGT = Column(Float)
    ATA = Column(Float)
    ATC = Column(Float)
    ATG = Column(Float)
    ATT = Column(Float)
    CAA = Column(Float)
    CAC = Column(Float)
    CAG = Column(Float)
    CAT = Column(Float)
    CCA = Column(Float)
    CCC = Column(Float)
    CCG = Column(Float)
    CCT = Column(Float)
    CGA = Column(Float)
    CGC = Column(Float)
    CGG = Column(Float)
    CGT = Column(Float)
    CTA = Column(Float)
    CTC = Column(Float)
    CTG = Column(Float)
    CTT = Column(Float)
    GAA = Column(Float)
    GAC = Column(Float)
    GAG = Column(Float)
    GAT = Column(Float)
    GCA = Column(Float)
    GCC = Column(Float)
    GCG = Column(Float)
    GCT = Column(Float)
    GGA = Column(Float)
    GGC = Column(Float)
    GGG = Column(Float)
    GGT = Column(Float)
    GTA = Column(Float)
    GTC = Column(Float)
    GTG = Column(Float)
    GTT = Column(Float)
    TAA = Column(Float)
    TAC = Column(Float)
    TAG = Column(Float)
    TAT = Column(Float)
    TCA = Column(Float)
    TCC = Column(Float)
    TCG = Column(Float)
    TCT = Column(Float)
    TGA = Column(Float)
    TGC = Column(Float)
    TGG = Column(Float)
    TGT = Column(Float)
    TTA = Column(Float)
    TTC = Column(Float)
    TTG = Column(Float)
    TTT = Column(Float)


    def __init__(self, name, **kwargs):
        self.name = name
        total_count = 0
        for codon in all_codons:
            # support upper and lower case codons
            codon_count = kwargs.get(codon, 0)
            codon_count += kwargs.get(codon.lower(), 0)
            total_count += codon_count

            self.__setattr__("{0}_count".format(codon), codon_count)

        if total_count  == 0:
            raise ValueError('No valid codons defined')

        self.total_count = total_count

        for codon in all_codons:
            codon_count = self.__getattribute__("{0}_count".format(codon))
            percentage = float(codon_count) / total_count * 100
            self.__setattr__(codon, percentage)


    def __str__(self):
        return self.name
