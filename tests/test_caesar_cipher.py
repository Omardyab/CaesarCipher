from caesar_cipher import __version__
from caesar_cipher.Caesar_Cipher import *


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    assert encrypt("Hello from 401 at AsAc", 3)== "Khoor iurp 401 dw DvDf"


def test_encrypt_lower():
    assert encrypt("hello from 401 at asac", 3)== "khoor iurp 401 dw dvdf"
    
def test_decrypt():
    assert decrypt("Khoor iurp 401 dw DvDf", 3)== "Hello from 401 at AsAc"

def test_encrypt_capital():
    assert encrypt("HELLO FROM CODEFELLOWS", 4)== "LIPPS JVSQ GSHIJIPPSAW"

def test_crack():
    assert crack("Mx aew xli fiwx sj xmqiw, mx aew xli asvwx sj xmqiw")== "It was the best of times, it was the worst of times"

