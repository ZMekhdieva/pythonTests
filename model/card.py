import os
import tempfile
import pytest

from conftest import pdf_file


class Card(object):
        def __init__(self, FIO=None, cadastr_number=None, square=None, mfcnumber=None, mfcdate=None, questioncategory=None, explanationsoms=None, explanationsmio=None):
            self.FIO = FIO
            self.cadastr_number = cadastr_number
            self.square = square
            self.mfcnumber = mfcnumber
            self.mfcdate = mfcdate
            self.questioncategory = questioncategory
            self.explanationsoms = explanationsoms
            self.explanationsmio = explanationsmio





