import pytest
from ...shared_mocks import MockPrinter
from .. import create_ctx


@pytest.fixture
def tdata(mocker):
    from collections import namedtuple
    from krux.key import Key
    from embit.networks import NETWORKS

    TEST_12_WORD_MNEMONIC = (
        "olympic term tissue route sense program under choose bean emerge velvet absurd"
    )
    TEST_24_WORD_MNEMONIC = "brush badge sing still venue panther kitchen please help panel bundle excess sign couch stove increase human once effort candy goat top tiny major"
    SIGNING_MNEMONIC = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

    SINGLESIG_12_WORD_KEY = Key(TEST_12_WORD_MNEMONIC, False, NETWORKS["main"])
    SINGLESIG_24_WORD_KEY = Key(TEST_24_WORD_MNEMONIC, False, NETWORKS["main"])
    MULTISIG_12_WORD_KEY = Key(TEST_12_WORD_MNEMONIC, True, NETWORKS["main"])
    SINGLESIG_SIGNING_KEY = Key(SIGNING_MNEMONIC, False, NETWORKS["main"])
    MULTISIG_SIGNING_KEY = Key(SIGNING_MNEMONIC, True, NETWORKS["main"])

    SPECTER_SINGLESIG_WALLET_DATA = '{"label": "Specter Singlesig Wallet", "blockheight": 0, "descriptor": "wpkh([55f8fc5d/84h/0h/0h]xpub6DPMTPxGMqdtzMwpqT1dDQaVdyaEppEm2qYSaJ7ANsuES7HkNzrXJst1Ed8D7NAnijUdgSDUFgph1oj5LKKAD5gyxWNhNP2AuDqaKYqzphA/0/*)#9qx3vqss", "devices": [{"type": "other", "label": "Key1"}]}'
    SPECTER_MULTISIG_WALLET_DATA = '{"label": "Specter Multisig Wallet", "blockheight": 0, "descriptor": "wsh(sortedmulti(2,[55f8fc5d/48h/0h/0h/2h]xpub6EKmKYGYc1WY6t9d3d9SksR8keSaPZbFa6tqsGiH4xVxx8d2YyxSX7WG6yXEX3CmG54dPCxaapDw1XsjwCmfoqP7tbsAeqMVfKvqSAu4ndy/0/*,[3e15470d/48h/0h/0h/2h]xpub6F2P6Pz5KLPgCc6pTBd2xxCunaSYWc8CdkL28W5z15pJrN3aCYY7mCUAkCMtqrgT2wdhAGgRnJxAkCCUpGKoXKxQ57yffEGmPwtYA3DEXwu/0/*,[d3a80c8b/48h/0h/0h/2h]xpub6FKYY6y3oVi7ihSCszFKRSeZj5SzrfSsUFXhKqjMV4iigrLhxwMX3mrjioNyLTZ5iD3u4wU9S3tyzpJGxhd5geaXoQ68jGz2M6dfh2zJrUv/0/*))#3nfc6jdy", "devices": [{"type": "other", "label": "Key1"}, {"type": "other", "label": "Key2"}, {"type": "other", "label": "Key3"}]}'

    P2WPKH_PSBT = b'psbt\xff\x01\x00q\x02\x00\x00\x00\x01\xcf<X\xc3)\x82\xae P\x88\xd9\xbdI\xeb\x9b\x02\xac\xdfM=\xaev\xa5\x16\xc6\xb3\x06\xb1]\xe3\xa1N\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02|?]\x05\x00\x00\x00\x00\x16\x00\x14/4\xaa\x1c\xf0\nS\xb0U\xa2\x91\xa0:}E\xf0\xa6\x98\x8bR\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01\x1f\x00\xe1\xf5\x05\x00\x00\x00\x00\x16\x00\x14\xd0\xc4\xa3\xef\t\xe9\x97\xb6\xe9\x9e9~Q\x8f\xe3\xe4\x1a\x11\x8c\xa1"\x06\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x02\x03]I\xec\xcdT\xd0\t\x9eCgbw\xc7\xa6\xd4b]a\x1d\xa8\x8a]\xf4\x9b\xf9Qzw\x91\xa7w\xa5\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    SIGNED_P2WPKH_PSBT = b'psbt\xff\x01\x00q\x02\x00\x00\x00\x01\xcf<X\xc3)\x82\xae P\x88\xd9\xbdI\xeb\x9b\x02\xac\xdfM=\xaev\xa5\x16\xc6\xb3\x06\xb1]\xe3\xa1N\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02|?]\x05\x00\x00\x00\x00\x16\x00\x14/4\xaa\x1c\xf0\nS\xb0U\xa2\x91\xa0:}E\xf0\xa6\x98\x8bR\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00"\x02\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19G0D\x02 >e\xff;L\xd4\x7f\x12\x1f\xa7\xc9\x82(F\x18\xdb\x801G\xb0V\xd3\x93\x94\xd4\xecB\x0e\xfd\xfck\xa1\x02 l\xbd\xd8\x8a\xc5\x18l?.\xfd$%1\xedy\x17uvQ\xac&#t\xf3\xd3\x1d\x85\xd6\x16\xcdj\x81\x01\x00\x00\x00'
    P2WPKH_PSBT_B64 = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAABAR8A4fUFAAAAABYAFNDEo+8J6Ze26Z45flGP4+QaEYyhIgYC56slN7XUnpcDCargbp5J82zhyf671E7I4NHMoLT5wxkYc8XaClQAAIABAACAAAAAgAAAAAAAAAAAACICA11J7M1U0AmeQ2did8em1GJdYR2oil30m/lReneRp3elGHPF2gpUAACAAQAAgAAAAIABAAAAAAAAAAAA"
    P2WPKH_PSBT_B64_ZEROES_FINGERPRINT = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAABAR8A4fUFAAAAABYAFNDEo+8J6Ze26Z45flGP4+QaEYyhIgYC56slN7XUnpcDCargbp5J82zhyf671E7I4NHMoLT5wxkYAAAAAFQAAIABAACAAAAAgAAAAAAAAAAAACICA11J7M1U0AmeQ2did8em1GJdYR2oil30m/lReneRp3elGHPF2gpUAACAAQAAgAAAAIABAAAAAAAAAAAA"
    SIGNED_P2WPKH_PSBT_B64 = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAAiAgLnqyU3tdSelwMJquBunknzbOHJ/rvUTsjg0cygtPnDGUcwRAIgPmX/O0zUfxIfp8mCKEYY24AxR7BW05OU1OxCDv38a6ECIGy92IrFGGw/Lv0kJTHteRd1dlGsJiN089MdhdYWzWqBAQAAAA=="
    P2WSH_PSBT = b'psbt\xff\x01\x00\xb2\x02\x00\x00\x00\x02\xadC\x87\x14J\xfae\x07\xe1>\xaeP\xda\x1b\xf1\xb5\x1ag\xb3\x0f\xfb\x8e\x0c[\x8f\x98\xf5\xb3\xb1\xa68Y\x00\x00\x00\x00\x00\xfd\xff\xff\xffig%Y\x0f\xb8\xe4r\xab#N\xeb\xf3\xbf\x04\xd9J\xc0\xba\x94\xf6\xa5\xa4\xf8B\xea\xdb\x9a\xd3c`\xd4\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02@B\x0f\x00\x00\x00\x00\x00"\x00 \xa9\x903\xc3\x86b3>Y\t\xae<=\x03\xbdq\x8d\xb2\x14Y\xfd\xd5P\x1e\xe8\xa0RaMY\xb4\xe2\xd8\xd2!\x01\x00\x00\x00\x00"\x00 \x8d\x02\x85\r\xab\x88^\xc5y\xbbm\xcb\x05\xd6 ;\x05\xf5\x17\x01\x86\xac\xb8\x90}l\xc1\xb4R\x99\xed\xd2\x00\x00\x00\x00O\x01\x045\x87\xcf\x04>b\xdf~\x80\x00\x00\x02A+I\x84\xd5I\xba^\xef\x1c\xa6\xe8\xf3u]\x9a\xe0\x16\xdam\x16ir\xca\x0eQ@6~\xddP\xda\x025\xb8K1\xdc8*|\xfbC\xba:{\x17K\xe9AaA\xe8\x16\xf6r[\xd1%\x12\xb5\xb2\xc4\xa5\xac\x14\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\x9d\xb1\xd0\x00\x80\x00\x00\x02?\xd8\xd7;\xc7\xb8\x8c\xa4\x93Z\xa57\xbf8\x94\xd5\xe2\x88\x9f\xab4\x1ca\x8fJWo\x8f\x19\x18\xc2u\x02h\xc3\rV\x9d#j}\xccW\x1b+\xb1\xd2\xadO\xa9\xf9\xb3R\xa8\t6\xa2\x89\n\x99\xaa#\xdbx\xec\x14&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\xba\xc1H9\x80\x00\x00\x02\x1dO\xbe\xbd\xd9g\xe1\xafqL\t\x97\xd3\x8f\xcfg\x0b\\\xe9\xd3\x01\xc0D\x0b\xbc\xc3\xb6\xa2\x0e\xb7r\x1c\x03V\x8e\xa1\xf3`Q\x91n\xd1\xb6\x90\xc3\x9e\x12\xa8\xe7\x06\x03\xb2\x80\xbd0\xce_(\x1f)\x18\xa5Sc\xaa\x14s\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 \x89\x801pn\xdd\x9e\xb1"g\x85G\x15Q\xce\xa3_\x17\t\xa9o\x85\x96.2\xa0k\xf6~\xc7\x11$\x01\x05iR!\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2!\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87S\xae"\x06\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 3w\xad03\xd1\x05\x9c\xf1\xd25\xbb\x12%\xfc\xa2\xa4\xbf&\xc9R\xd5?o\xef\xc3:-UD\x8d\xc5\x01\x05iR!\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"!\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t!\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01S\xae"\x06\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01iR!\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe!\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v!\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2kS\xae"\x02\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2k\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    SIGNED_P2WSH_PSBT = b'psbt\xff\x01\x00\xb2\x02\x00\x00\x00\x02\xadC\x87\x14J\xfae\x07\xe1>\xaeP\xda\x1b\xf1\xb5\x1ag\xb3\x0f\xfb\x8e\x0c[\x8f\x98\xf5\xb3\xb1\xa68Y\x00\x00\x00\x00\x00\xfd\xff\xff\xffig%Y\x0f\xb8\xe4r\xab#N\xeb\xf3\xbf\x04\xd9J\xc0\xba\x94\xf6\xa5\xa4\xf8B\xea\xdb\x9a\xd3c`\xd4\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02@B\x0f\x00\x00\x00\x00\x00"\x00 \xa9\x903\xc3\x86b3>Y\t\xae<=\x03\xbdq\x8d\xb2\x14Y\xfd\xd5P\x1e\xe8\xa0RaMY\xb4\xe2\xd8\xd2!\x01\x00\x00\x00\x00"\x00 \x8d\x02\x85\r\xab\x88^\xc5y\xbbm\xcb\x05\xd6 ;\x05\xf5\x17\x01\x86\xac\xb8\x90}l\xc1\xb4R\x99\xed\xd2\x00\x00\x00\x00\x00"\x02\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87G0D\x02 h?m\x19\x04C\x89\x95\x8b\xba\xed\xbb\xba8)\t\xae^\xe3`\x16G\xc8\x8bq\x9c\x0e\xbc\xc5\xb1j\xa2\x02 \x05\rP(\xe0\x9cc])q\xe5\xe2S\x9f\xaf+\xe4_\xa9\xc6\xf9\r"%\xf4\xa2\x00;\xa2\xaf2W\x01\x00"\x02\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01G0D\x02 ~O\x1b\x8c\xbb\x87x\xa3\xbb\xff\x04\xd8\x10Cq\xc8Y\x0f;N6\x97\xd8S\xfeti\x80\xb3\x12\xe0>\x02 l\x93=\x02m\xb4<\x90\xf4%\xf9Z${\xb7\xecO\x19\x15\xa3\xa3S\xf2Q\x81\xdcX\xfb\xd5&\x9e\xc5\x01\x00\x00\x00'
    P2WSH_PSBT_B64 = "cHNidP8BALICAAAAAq1DhxRK+mUH4T6uUNob8bUaZ7MP+44MW4+Y9bOxpjhZAAAAAAD9////aWclWQ+45HKrI07r878E2UrAupT2paT4QurbmtNjYNQBAAAAAP3///8CQEIPAAAAAAAiACCpkDPDhmIzPlkJrjw9A71xjbIUWf3VUB7ooFJhTVm04tjSIQEAAAAAIgAgjQKFDauIXsV5u23LBdYgOwX1FwGGrLiQfWzBtFKZ7dIAAAAATwEENYfPBD5i336AAAACQStJhNVJul7vHKbo83VdmuAW2m0WaXLKDlFANn7dUNoCNbhLMdw4Knz7Q7o6exdL6UFhQegW9nJb0SUStbLEpawUAgjLdzAAAIABAACAAAAAgAIAAIBPAQQ1h88EnbHQAIAAAAI/2Nc7x7iMpJNapTe/OJTV4oifqzQcYY9KV2+PGRjCdQJoww1WnSNqfcxXGyux0q1PqfmzUqgJNqKJCpmqI9t47BQmu4PEMAAAgAEAAIAAAACAAgAAgE8BBDWHzwS6wUg5gAAAAh1Pvr3ZZ+GvcUwJl9OPz2cLXOnTAcBEC7zDtqIOt3IcA1aOofNgUZFu0baQw54SqOcGA7KAvTDOXygfKRilU2OqFHPF2gowAACAAQAAgAAAAIACAACAAAEBK4CWmAAAAAAAIgAgiYAxcG7dnrEiZ4VHFVHOo18XCalvhZYuMqBr9n7HESQBBWlSIQJOjQgMfX26XEf+trHIEk3rYkEX5Y2NfrFKQARPcd2X8iEDBWHUgq25PfHvE+hlcBryJG7wo2y8jKUSPY7sd85OOMchA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHU64iBgJOjQgMfX26XEf+trHIEk3rYkEX5Y2NfrFKQARPcd2X8hwmu4PEMAAAgAEAAIAAAACAAgAAgAAAAAABAAAAIgYDBWHUgq25PfHvE+hlcBryJG7wo2y8jKUSPY7sd85OOMccAgjLdzAAAIABAACAAAAAgAIAAIAAAAAAAQAAACIGA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHHHPF2gowAACAAQAAgAAAAIACAACAAAAAAAEAAAAAAQErgJaYAAAAAAAiACAzd60wM9EFnPHSNbsSJfyipL8myVLVP2/vwzotVUSNxQEFaVIhAiKCMRLlzIhLkRbLIUIMx5KYJM0v6LcjW/mS6K7eFGwiIQKDzUflU23LeecRgzDo5IBCEvaWGfHW7JkNxzXvuc7FdCEDC5DtLoa61/Kk/pdpu0F9e6nKoRJIB9v7Ni377rZefgFTriIGAiKCMRLlzIhLkRbLIUIMx5KYJM0v6LcjW/mS6K7eFGwiHAIIy3cwAACAAQAAgAAAAIACAACAAAAAAAAAAAAiBgKDzUflU23LeecRgzDo5IBCEvaWGfHW7JkNxzXvuc7FdBwmu4PEMAAAgAEAAIAAAACAAgAAgAAAAAAAAAAAIgYDC5DtLoa61/Kk/pdpu0F9e6nKoRJIB9v7Ni377rZefgEcc8XaCjAAAIABAACAAAAAgAIAAIAAAAAAAAAAAAABAWlSIQKtIdmtKKuZrH7f2R4iIU8RWVOrCdHVWBCS+0e9pZJy/iEDoH074LrWPIA10hyXtBCJDT06GdLkA6+z/PxoJqomPHYhA6GoQ/otQdk71nUpYZFfbkSKdBkkSj4CuPTPYrzGp6JrU64iAgKtIdmtKKuZrH7f2R4iIU8RWVOrCdHVWBCS+0e9pZJy/hwCCMt3MAAAgAEAAIAAAACAAgAAgAEAAAAAAAAAIgIDoH074LrWPIA10hyXtBCJDT06GdLkA6+z/PxoJqomPHYcc8XaCjAAAIABAACAAAAAgAIAAIABAAAAAAAAACICA6GoQ/otQdk71nUpYZFfbkSKdBkkSj4CuPTPYrzGp6JrHCa7g8QwAACAAQAAgAAAAIACAACAAQAAAAAAAAAAAA=="
    SIGNED_P2WSH_PSBT_B64 = "cHNidP8BALICAAAAAq1DhxRK+mUH4T6uUNob8bUaZ7MP+44MW4+Y9bOxpjhZAAAAAAD9////aWclWQ+45HKrI07r878E2UrAupT2paT4QurbmtNjYNQBAAAAAP3///8CQEIPAAAAAAAiACCpkDPDhmIzPlkJrjw9A71xjbIUWf3VUB7ooFJhTVm04tjSIQEAAAAAIgAgjQKFDauIXsV5u23LBdYgOwX1FwGGrLiQfWzBtFKZ7dIAAAAAACICA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHRzBEAiBoP20ZBEOJlYu67bu6OCkJrl7jYBZHyItxnA68xbFqogIgBQ1QKOCcY10pceXiU5+vK+Rfqcb5DSIl9KIAO6KvMlcBACICAwuQ7S6GutfypP6XabtBfXupyqESSAfb+zYt++62Xn4BRzBEAiB+TxuMu4d4o7v/BNgQQ3HIWQ87TjaX2FP+dGmAsxLgPgIgbJM9Am20PJD0JflaJHu37E8ZFaOjU/JRgdxY+9UmnsUBAAAA"

    # Use https://bip174.org/ to see the contents of the PSBT_B64
    # Use the command below on linux to see the binary PSBT as BASE64
    # base64 binary.psbt | tr -d '\n\r'

    return namedtuple(
        "TestData",
        [
            "TEST_12_WORD_MNEMONIC",
            "TEST_24_WORD_MNEMONIC",
            "SIGNING_MNEMONIC",
            "SINGLESIG_12_WORD_KEY",
            "SINGLESIG_24_WORD_KEY",
            "MULTISIG_12_WORD_KEY",
            "SINGLESIG_SIGNING_KEY",
            "MULTISIG_SIGNING_KEY",
            "SPECTER_SINGLESIG_WALLET_DATA",
            "SPECTER_MULTISIG_WALLET_DATA",
            "P2WPKH_PSBT",
            "SIGNED_P2WPKH_PSBT",
            "P2WPKH_PSBT_B64",
            "P2WPKH_PSBT_B64_ZEROES_FINGERPRINT",
            "SIGNED_P2WPKH_PSBT_B64",
            "P2WSH_PSBT",
            "SIGNED_P2WSH_PSBT",
            "P2WSH_PSBT_B64",
            "SIGNED_P2WSH_PSBT_B64",
        ],
    )(
        TEST_12_WORD_MNEMONIC,
        TEST_24_WORD_MNEMONIC,
        SIGNING_MNEMONIC,
        SINGLESIG_12_WORD_KEY,
        SINGLESIG_24_WORD_KEY,
        MULTISIG_12_WORD_KEY,
        SINGLESIG_SIGNING_KEY,
        MULTISIG_SIGNING_KEY,
        SPECTER_SINGLESIG_WALLET_DATA,
        SPECTER_MULTISIG_WALLET_DATA,
        P2WPKH_PSBT,
        SIGNED_P2WPKH_PSBT,
        P2WPKH_PSBT_B64,
        P2WPKH_PSBT_B64_ZEROES_FINGERPRINT,
        SIGNED_P2WPKH_PSBT_B64,
        P2WSH_PSBT,
        SIGNED_P2WSH_PSBT,
        P2WSH_PSBT_B64,
        SIGNED_P2WSH_PSBT_B64,
    )


def test_load_mnemonic_view(mocker, amigo):
    from krux.pages.home_pages.home import Home
    from krux.input import BUTTON_ENTER, BUTTON_PAGE_PREV

    BTN_SEQUENCE = [
        BUTTON_PAGE_PREV,  # Go to Back
        BUTTON_ENTER,  # Exit
    ]

    ctx = create_ctx(mocker, BTN_SEQUENCE)
    home = Home(ctx)
    home.backup_mnemonic()

    assert ctx.input.wait_for_button.call_count == len(BTN_SEQUENCE)


def test_load_pub_key_view(mocker, amigo, tdata):
    from krux.pages.home_pages.home import Home
    from krux.wallet import Wallet
    from krux.input import BUTTON_ENTER, BUTTON_PAGE_PREV

    BTN_SEQUENCE = [
        BUTTON_PAGE_PREV,  # Go to Back
        BUTTON_ENTER,  # Exit
    ]

    wallet = Wallet(tdata.SINGLESIG_SIGNING_KEY)
    ctx = create_ctx(mocker, BTN_SEQUENCE, wallet=wallet)
    home = Home(ctx)
    home.public_key()

    assert ctx.input.wait_for_button.call_count == len(BTN_SEQUENCE)


def test_load_wallet_descritor_manager(mocker, amigo, tdata):
    from krux.pages.home_pages.home import Home
    from krux.wallet import Wallet
    from krux.input import BUTTON_PAGE, BUTTON_ENTER

    BTN_SEQUENCE = [
        BUTTON_PAGE,  # Move to "No"
        BUTTON_ENTER,  # Decline to load
    ]

    wallet = Wallet(tdata.SINGLESIG_SIGNING_KEY)
    ctx = create_ctx(mocker, BTN_SEQUENCE, wallet=wallet)
    home = Home(ctx)
    home.wallet_descriptor()

    assert ctx.input.wait_for_button.call_count == len(BTN_SEQUENCE)


def test_load_address_view(mocker, amigo, tdata):
    from krux.pages.home_pages.home import Home
    from krux.wallet import Wallet
    from krux.input import BUTTON_ENTER, BUTTON_PAGE_PREV

    BTN_SEQUENCE = [
        BUTTON_PAGE_PREV,  # Go to Back
        BUTTON_ENTER,  # Exit
    ]

    wallet = Wallet(tdata.SINGLESIG_SIGNING_KEY)
    ctx = create_ctx(mocker, BTN_SEQUENCE, wallet=wallet)
    home = Home(ctx)
    home.addresses_menu()

    assert ctx.input.wait_for_button.call_count == len(BTN_SEQUENCE)


def test_sign_menu(mocker, amigo, tdata):
    from krux.pages.home_pages.home import Home
    from krux.input import BUTTON_ENTER, BUTTON_PAGE_PREV

    BTN_SEQUENCE = [
        BUTTON_PAGE_PREV,  # Go to Back
        BUTTON_ENTER,  # Exit
    ]

    ctx = create_ctx(mocker, BTN_SEQUENCE)
    home = Home(ctx)
    home.sign()

    assert ctx.input.wait_for_button.call_count == len(BTN_SEQUENCE)


def test_load_sign_message_menu(mocker, amigo):
    from krux.pages.home_pages.home import Home
    from krux.input import BUTTON_ENTER, BUTTON_PAGE_PREV

    BTN_SEQUENCE = [
        BUTTON_PAGE_PREV,  # Go to Back
        BUTTON_ENTER,  # Exit
    ]

    ctx = create_ctx(mocker, BTN_SEQUENCE)
    home = Home(ctx)
    home.sign_message()

    assert ctx.input.wait_for_button.call_count == len(BTN_SEQUENCE)


def test_sign_psbt(mocker, m5stickv, tdata):
    from krux.pages.home_pages.home import Home
    from krux.wallet import Wallet
    from krux.input import BUTTON_ENTER, BUTTON_PAGE
    from krux.qr import FORMAT_PMOFN, FORMAT_NONE
    from krux.sd_card import PSBT_FILE_EXTENSION, SIGNED_FILE_SUFFIX

    cases = [
        # Single-sig, not loaded, no format => pmofn, sign, No print prompt
        (
            # Case 0
            tdata.SINGLESIG_SIGNING_KEY,  # 0 wallet
            None,  # 1 wallet
            tdata.P2WPKH_PSBT_B64,  # 2 capture_qr_code return 1
            FORMAT_NONE,  # 3 capture_qr_code return 2
            True,  # 4 if was signed!
            tdata.SIGNED_P2WPKH_PSBT_B64,  # 5
            None,  # 6 printer
            # 7 btn_seq
            [
                # BUTTON_ENTER,  # Wallet not loaded, proceed?
                BUTTON_ENTER,  # Load from QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_ENTER,  # Sign to QR code
                BUTTON_ENTER,  # Leave
            ],
            None,  # 8 SD avaiable
        ),
        # Single-sig, not loaded, pmofn, sign, No print prompt
        (
            # Case 1
            tdata.SINGLESIG_SIGNING_KEY,
            None,
            tdata.P2WPKH_PSBT_B64,
            FORMAT_PMOFN,
            True,
            tdata.SIGNED_P2WPKH_PSBT_B64,
            None,
            [
                BUTTON_ENTER,  # Load frm QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_ENTER,  # Sign to QR code
                BUTTON_ENTER,  # Leave
            ],
            None,
        ),
        # Single-sig, not loaded, pmofn, sign, Print
        (
            # Case 2
            tdata.SINGLESIG_SIGNING_KEY,
            None,
            tdata.P2WPKH_PSBT_B64,
            FORMAT_PMOFN,
            True,
            tdata.SIGNED_P2WPKH_PSBT_B64,
            MockPrinter(),
            [
                BUTTON_ENTER,  # Load frm QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_ENTER,  # Sign to QR code
                BUTTON_ENTER,  # Jump QR signed
                BUTTON_ENTER,  # Print Yes
            ],
            None,
        ),
        # Single-sig, not loaded, pmofn, sign, Decline to print
        (
            # Case 3
            tdata.SINGLESIG_SIGNING_KEY,
            None,
            tdata.P2WPKH_PSBT_B64,
            FORMAT_PMOFN,
            True,
            tdata.SIGNED_P2WPKH_PSBT_B64,
            MockPrinter(),
            [
                BUTTON_ENTER,  # Load frm QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_ENTER,  # Sign to QR code
                BUTTON_ENTER,  # Jump QR signed
                BUTTON_PAGE,  # Print No
            ],
            None,
        ),
        # Single-sig, not loaded, pmofn, decline to sign
        (
            # Case 4
            tdata.SINGLESIG_SIGNING_KEY,
            None,
            tdata.P2WPKH_PSBT_B64,
            FORMAT_PMOFN,
            False,
            None,
            None,
            [
                BUTTON_ENTER,  # Load frm QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_PAGE,  # Move to Sign to QR SD card
                BUTTON_PAGE,  # Move to Back
                BUTTON_ENTER,  # Leave
            ],
            None,
        ),
        # Single-sig, not loaded, failed to capture PSBT QR
        (
            # Case 5
            tdata.SINGLESIG_SIGNING_KEY,
            None,
            None,
            None,
            False,
            None,
            None,
            [BUTTON_ENTER],  # Load from QR code - failed
            None,
        ),
        # Multisig, not loaded, decline to proceed after warning
        (
            # Case 6
            tdata.MULTISIG_SIGNING_KEY,
            None,
            None,
            None,
            False,
            None,
            None,
            [BUTTON_PAGE],  # Wallet not loaded, proceed?
            None,
        ),
        # Multisig, not loaded, pmofn, sign, No print prompt
        (
            # Case 7
            tdata.MULTISIG_SIGNING_KEY,
            None,
            tdata.P2WSH_PSBT_B64,
            FORMAT_PMOFN,
            True,
            tdata.SIGNED_P2WSH_PSBT_B64,
            None,
            [
                BUTTON_ENTER,  # Wallet not loaded, proceed?
                BUTTON_ENTER,  # Load from QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT Policy ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_ENTER,  # Sign to QR code
                BUTTON_ENTER,  # Jump QR signed
            ],
            None,
        ),
        # Multisig, not loaded, pmofn, sign, Print
        (
            # Case 8
            tdata.MULTISIG_SIGNING_KEY,
            None,
            tdata.P2WSH_PSBT_B64,
            FORMAT_PMOFN,
            True,
            tdata.SIGNED_P2WSH_PSBT_B64,
            MockPrinter(),
            [
                BUTTON_ENTER,  # Wallet not loaded, proceed?
                BUTTON_ENTER,  # Load from QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT Policy ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_ENTER,  # Sign to QR code
                BUTTON_ENTER,  # Jump QR signed
                BUTTON_ENTER,  # Print Yes
            ],
            None,
        ),
        # Multisig, not loaded, pmofn, sign, Decline to print
        (
            # Case 9
            tdata.MULTISIG_SIGNING_KEY,
            None,
            tdata.P2WSH_PSBT_B64,
            FORMAT_PMOFN,
            True,
            tdata.SIGNED_P2WSH_PSBT_B64,
            MockPrinter(),
            [
                BUTTON_ENTER,  # Wallet not loaded, proceed?
                BUTTON_ENTER,  # Load from QR code
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT Policy ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_ENTER,  # Sign to QR code
                BUTTON_ENTER,  # Jump QR signed
                BUTTON_PAGE,  # Print No
            ],
            None,
        ),
        # Single-sig, not loaded, load from microSD, sign to microSD
        (
            # Case 10
            tdata.SINGLESIG_SIGNING_KEY,  # 0 wallet
            None,
            tdata.P2WPKH_PSBT,  # 2 capture_qr_code return 1
            FORMAT_NONE,  # 3 capture_qr_code return 2
            True,
            tdata.SIGNED_P2WPKH_PSBT_B64,
            None,  # 6 printer
            [
                BUTTON_PAGE,  # Move to "Load from SD card"
                BUTTON_ENTER,  # Load from SD card
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_PAGE,  # Move to "Sign to QR SD card"
                BUTTON_ENTER,  # Sign to SD card
            ],
            tdata.SIGNED_P2WPKH_PSBT,  # 8 SD avaiable
        ),
        # Multisig, not loaded, load from microSD, sign, save to microSD, No print prompt
        (
            # Case 11
            tdata.MULTISIG_SIGNING_KEY,
            None,
            tdata.P2WSH_PSBT,
            FORMAT_NONE,
            True,
            tdata.SIGNED_P2WSH_PSBT_B64,
            None,
            [
                BUTTON_ENTER,  # Wallet not loaded, proceed?
                BUTTON_PAGE,  # Move to "Load from SD card"
                BUTTON_ENTER,  # Load from SD card
                BUTTON_ENTER,  # Path mismatch ACK
                BUTTON_ENTER,  # PSBT Policy ACK
                BUTTON_ENTER,  # PSBT resume
                BUTTON_ENTER,  # output 1
                BUTTON_ENTER,  # output 2
                BUTTON_PAGE,  # Move to "Sign to QR SD card"
                BUTTON_ENTER,  # Sign to SD card
            ],
            tdata.SIGNED_P2WSH_PSBT,  # 8 SD avaiable
        ),
    ]
    # Case X
    # [0] Wallet
    # [1] Imported wallet descriptor (not used yet)
    # [2] PSBT Data imported from QR code or SD card
    # [3] QR code format
    # [4] Flag - Was it signed?
    # [5] Signed PSBT Data exported to QR code
    # [6] Printer
    # [7] Button Sequence
    # [8] Signed PSBT Data exported to SD card

    PSBT_FILE_NAME = "test.psbt"
    num = 0
    for case in cases:
        print("test_sign_psbt", num)
        num += 1
        wallet = Wallet(case[0])
        if case[1] is not None:
            wallet.load(case[1], FORMAT_PMOFN)

        ctx = create_ctx(mocker, case[7], wallet, case[6])
        home = Home(ctx)
        mocker.patch.object(home, "capture_qr_code", new=lambda: (case[2], case[3]))
        mocker.patch.object(
            home,
            "display_qr_codes",
            new=lambda data, qr_format, title=None: ctx.input.wait_for_button(),
        )
        mocker.spy(home, "capture_qr_code")
        mocker.spy(home, "display_qr_codes")
        if case[6]:
            mock_send_to_printer = mocker.patch(
                "krux.pages.print_page.PrintPage._send_qr_to_printer"
            )

        # case SD available
        if case[8] is not None:
            mocker.patch.object(home, "has_sd_card", new=lambda: True)
            mock_utils = mocker.patch("krux.pages.utils.Utils")
            mock_utils.return_value.load_file.return_value = (PSBT_FILE_NAME, case[2])
            mock_file_save = mocker.patch(
                "krux.pages.file_operations.SaveFile.save_file"
            )
        home.sign_psbt()

        assert ctx.input.wait_for_button.call_count == len(case[7])

        loaded_via_sd = (
            len(case[7]) > 1
            and case[7][0] == BUTTON_PAGE
            and case[7][1] == BUTTON_ENTER
        )
        if loaded_via_sd:
            home.capture_qr_code.assert_not_called()

        if case[4] and case[8] is None:  # if signed from/to QR codes
            home.display_qr_codes.assert_called_once_with(case[5], FORMAT_PMOFN)

        if case[8] is not None:  # if signed from/to SD card
            mock_utils.return_value.load_file.assert_called_once_with(
                ".psbt", prompt=False
            )
            mock_file_save.assert_called_once_with(
                case[8],
                "QRCode",
                PSBT_FILE_NAME,
                "Signed PSBT" + ":",  # Title
                PSBT_FILE_EXTENSION,
                SIGNED_FILE_SUFFIX,
            )
            home.display_qr_codes.assert_not_called()

        if case[6] is not None:  # if has printer
            if case[7][-1] == BUTTON_ENTER:  # if printed
                mock_send_to_printer.assert_called()
            else:  # if declined to print
                mock_send_to_printer.assert_not_called()

    # TODO: Create cross test cases: Load from QR code, sign, save to SD card and vice versa
    # TODO: Import wallet descriptor and test signing


def test_psbt_warnings(mocker, m5stickv, tdata):
    from krux.pages.home_pages.home import Home
    from krux.wallet import Wallet
    from krux.input import BUTTON_ENTER, BUTTON_PAGE
    from krux.sd_card import PSBT_FILE_EXTENSION, SIGNED_FILE_SUFFIX

    PSBT_FILE_NAME = "test.psbt"

    wallet = Wallet(tdata.MULTISIG_SIGNING_KEY)

    btn_seq = [
        BUTTON_ENTER,  # Wallet not loaded, proceed?
        BUTTON_PAGE,  # Move to "Load from SD card"
        BUTTON_ENTER,  # Load from SD card
        BUTTON_ENTER,  # Path mismatch ACK
        BUTTON_ENTER,  # PSBT Policy ACK
        BUTTON_ENTER,  # PSBT resume
        BUTTON_ENTER,  # output 1
        BUTTON_ENTER,  # output 2
        BUTTON_PAGE,  # Move to "Sign to QR SD card"
        BUTTON_ENTER,  # Sign to SD card
    ]

    ctx = create_ctx(mocker, btn_seq, wallet)
    home = Home(ctx)

    mocker.spy(home, "display_qr_codes")
    mocker.spy(ctx.display, "draw_centered_text")

    # SD available
    mocker.patch.object(home, "has_sd_card", new=lambda: True)
    mock_utils = mocker.patch("krux.pages.utils.Utils")
    mock_utils.return_value.load_file.return_value = (
        PSBT_FILE_NAME,
        tdata.P2WSH_PSBT_B64,
    )
    mock_file_save = mocker.patch("krux.pages.file_operations.SaveFile.save_file")

    # Wallet output descriptor not loaded
    assert ctx.wallet.is_loaded() == wallet.is_loaded() == False

    # Wallet is multisig
    assert ctx.wallet.is_multisig() == wallet.is_multisig() == True

    home.sign_psbt()

    # all inputs were used/consumed
    assert ctx.input.wait_for_button.call_count == len(btn_seq)

    # Multisig with wallet output descriptor not loaded had to show a warning
    ctx.display.draw_centered_text.assert_any_call(
        "Warning:\nWallet output descriptor not found.\n\nSome checks cannot be performed."
    )

    # These two calls must occur in sequence
    ctx.display.draw_centered_text.assert_has_calls(
        [
            mocker.call(
                "Warning: Path mismatch\nWallet: m/48'/0'/0'/2'\nPSBT: m/48'/1'/0'/2'"
            ),
            mocker.call(
                "PSBT policy:\np2wsh\n2 of 3\n⊚ 26bb83c4\n⊚ 0208cb77\n⊚ 73c5da0a"
            ),
        ]
    )

    # signed from/to SD card
    mock_utils.return_value.load_file.assert_called_once_with(".psbt", prompt=False)
    mock_file_save.assert_called_once_with(
        tdata.SIGNED_P2WSH_PSBT,
        "QRCode",
        PSBT_FILE_NAME,
        "Signed PSBT" + ":",  # Title
        PSBT_FILE_EXTENSION,
        SIGNED_FILE_SUFFIX,
    )

    # no qrcode
    home.display_qr_codes.assert_not_called()


def test_sign_wrong_key(mocker, m5stickv, tdata):
    from krux.pages.home_pages.home import Home
    from krux.wallet import Wallet
    from krux.input import BUTTON_ENTER
    from krux.qr import FORMAT_PMOFN, FORMAT_NONE

    btn_seq = [
        BUTTON_ENTER,  # Load from QR code
        BUTTON_ENTER,  # Path mismatch ACK
        BUTTON_ENTER,  # PSBT resume
        BUTTON_ENTER,  # output 1
        BUTTON_ENTER,  # output 2
        BUTTON_ENTER,  # Sign to QR code
    ]
    wallet = Wallet(tdata.SINGLESIG_12_WORD_KEY)
    ctx = create_ctx(mocker, btn_seq, wallet)
    home = Home(ctx)
    mocker.patch.object(
        home, "capture_qr_code", new=lambda: (tdata.P2WPKH_PSBT_B64, FORMAT_NONE)
    )
    mocker.patch.object(
        home,
        "display_qr_codes",
        new=lambda data, qr_format, title=None: ctx.input.wait_for_button(),
    )
    mocker.spy(home, "capture_qr_code")
    mocker.spy(home, "display_qr_codes")

    # Wrong key, will raise error "cannot sign"
    with pytest.raises(ValueError):
        home.sign_psbt()

    assert ctx.input.wait_for_button.call_count == len(btn_seq)

    # ERROR raised: no qrcode
    home.display_qr_codes.assert_not_called()


def test_sign_zeroes_fingerprint(mocker, m5stickv, tdata):
    from krux.pages.home_pages.home import Home
    from krux.wallet import Wallet
    from krux.input import BUTTON_ENTER
    from krux.qr import FORMAT_PMOFN, FORMAT_NONE

    # TODO: when fixed, fix this seq
    btn_seq = [
        BUTTON_ENTER,  # Load from QR code
        BUTTON_ENTER,  # Path mismatch ACK
        BUTTON_ENTER,  # PSBT resume
        BUTTON_ENTER,  # output 1
        BUTTON_ENTER,  # output 2
        BUTTON_ENTER,  # Sign to QR code
    ]
    wallet = Wallet(tdata.SINGLESIG_SIGNING_KEY)
    ctx = create_ctx(mocker, btn_seq, wallet)
    home = Home(ctx)
    mocker.patch.object(
        home,
        "capture_qr_code",
        new=lambda: (tdata.P2WPKH_PSBT_B64_ZEROES_FINGERPRINT, FORMAT_NONE),
    )
    mocker.patch.object(
        home,
        "display_qr_codes",
        new=lambda data, qr_format, title=None: ctx.input.wait_for_button(),
    )
    mocker.spy(home, "capture_qr_code")
    mocker.spy(home, "display_qr_codes")

    # Wrong key, will raise error "cannot sign"
    with pytest.raises(ValueError):
        home.sign_psbt()

    assert ctx.input.wait_for_button.call_count == len(btn_seq)

    # ERROR raised: no qrcode
    home.display_qr_codes.assert_not_called()

    # TODO: when fixed, uncomment this line
    # home.display_qr_codes.assert_called_once_with(tdata.SIGNED_P2WPKH_PSBT_B64, FORMAT_PMOFN)
