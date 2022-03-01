from .shared_mocks import *
from krux.key import Key
from krux.wallet import Wallet
from embit.networks import NETWORKS
import pytest
from ur.ur import UR
from urtypes.crypto.psbt import PSBT

TEST_MNEMONIC = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

P2WPKH_PSBT = b'psbt\xff\x01\x00q\x02\x00\x00\x00\x01\xcf<X\xc3)\x82\xae P\x88\xd9\xbdI\xeb\x9b\x02\xac\xdfM=\xaev\xa5\x16\xc6\xb3\x06\xb1]\xe3\xa1N\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02|?]\x05\x00\x00\x00\x00\x16\x00\x14/4\xaa\x1c\xf0\nS\xb0U\xa2\x91\xa0:}E\xf0\xa6\x98\x8bR\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01\x1f\x00\xe1\xf5\x05\x00\x00\x00\x00\x16\x00\x14\xd0\xc4\xa3\xef\t\xe9\x97\xb6\xe9\x9e9~Q\x8f\xe3\xe4\x1a\x11\x8c\xa1"\x06\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x02\x03]I\xec\xcdT\xd0\t\x9eCgbw\xc7\xa6\xd4b]a\x1d\xa8\x8a]\xf4\x9b\xf9Qzw\x91\xa7w\xa5\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
P2WPKH_PSBT_B43 = "1N0HGUN:R2Q*R86JDWEOBMHAETS.D$7T+SEGWXJO3JPKXA+O3JNN$$VLXOA4R/O+2+T$0BL68OC3*:/B4SOZWX3MY9B1R0AXW5-KVBGEJJWUNUTMA5-XE+IX*M5$/.++VV9F/RHZC9:E9JT$NLGK39-VJKFHLA*C90GDVYE01C17+N*JBV0RQLT8D*1*BVK+K2K/$8.VYDK3JPC2X634YJKT57OJNX61X$4J39$.4*TZK55UAA0ALQC0PLZC61AYGB$J:SKX63U23TBU.C9NB.9C0N$RKANBNTQTYPVL1ZG6SHLT093GQFJILC0QMUYEY9F-K8.-3:JMZ4ESOL8AO+CD*7U06IVD3U6Y.$HH5PU/NPL037224KA-1A09MM76ZJ.:HY4TS-Y/8MZC6P/D6*DQF6A9"
P2WPKH_PSBT_B58 = "UUucvki6KWyS35DhetbWPw1DiaccbHKywScF96E8VUwEnN1gss947UasRfkNxtrkzCeHziHyMCuoiQ2mSYsbYXuV3YwYBZwFh1c6xtBAEK1aDgPwMgqf74xTzf3m4KH4iUU5nHTqroDpoRZR59meafTCUBChZ5NJ8MoUdKE6avyYdSm5kUb4npmFpMpJ9S3qd2RedHMoQFRiXK3jwdH81emAEsFYSW3Kb7caPcWjkza4S4EEWWbaggofGFmxE5gNNg4A4LNC2ZUGLsALZffNvg3yh3qg6rFxhkiyzWc44kx9Khp6Evm1j4Njh8kjifkngLTPFtX3uWNLAB1XrvpPMx6kkkhr7RnFVrA4JsDp5BwVGAXBoSBLTqweFevZ5"
P2WPKH_PSBT_B64 = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAABAR8A4fUFAAAAABYAFNDEo+8J6Ze26Z45flGP4+QaEYyhIgYC56slN7XUnpcDCargbp5J82zhyf671E7I4NHMoLT5wxkYc8XaClQAAIABAACAAAAAgAAAAAAAAAAAACICA11J7M1U0AmeQ2did8em1GJdYR2oil30m/lReneRp3elGHPF2gpUAACAAQAAgAAAAIABAAAAAAAAAAAA"
P2WPKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2WPKH_PSBT).to_cbor())

SIGNED_P2WPKH_PSBT = b'psbt\xff\x01\x00q\x02\x00\x00\x00\x01\xcf<X\xc3)\x82\xae P\x88\xd9\xbdI\xeb\x9b\x02\xac\xdfM=\xaev\xa5\x16\xc6\xb3\x06\xb1]\xe3\xa1N\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02|?]\x05\x00\x00\x00\x00\x16\x00\x14/4\xaa\x1c\xf0\nS\xb0U\xa2\x91\xa0:}E\xf0\xa6\x98\x8bR\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00"\x02\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19G0D\x02 >e\xff;L\xd4\x7f\x12\x1f\xa7\xc9\x82(F\x18\xdb\x801G\xb0V\xd3\x93\x94\xd4\xecB\x0e\xfd\xfck\xa1\x02 l\xbd\xd8\x8a\xc5\x18l?.\xfd$%1\xedy\x17uvQ\xac&#t\xf3\xd3\x1d\x85\xd6\x16\xcdj\x81\x01\x00\x00\x00'
SIGNED_P2WPKH_PSBT_B43 = "L/DXBQZOGZH1+TEUX6.$EO8.QU4PTU$VB9TTKTJSHSZ$98S8+9Y/4S7SV40I3QQT2XU+2W1KHLPLWCO9NIRR9R3Z7VIR3/H+C9BW-ZSGG5UEHLQ:A$858KOL.QSTZSPD*0RH.5VYKF$IPGMCI3.+UG-MZ/1DD*ZC0O91CJ*7D1+8O..EZ4T+K8OBLXC71B179LH*.J:H5IJGUJHWU8FZKE93:B**FDUD$H57HF283-2X:+09T7X+6/-1-.8PHK/5/LEU2HC5PQWN32/OSA-SVG0HT5UAO5P7.03KOA6$K*-TV6/DHZ$IXQ81$R88C53WCB7N9P:7Y-Z7BM.DQBTO24"
SIGNED_P2WPKH_PSBT_B58 = "DvASypbzvaAvzDRWWKHw6AX8KQFL3CXdmX5JHoqXkAuEGhiZu6jbRuYkj2rPYkCAgMxnz7DHQj5hTqZnGinPsJmL8ftwGptteNkHCnsuaCKQXNSd1m4EDsRYdjVftq6gdLRcs59kFupD3mELiFV7kyRk3E53YZAmjQQ7AUby4xQqm3yCmeTxYJXX51FyUFTVNQbTkXDoiojqHhH89g7TXYH4S5s2tm13KasUJXf9jpxgovedyXp4vAy6xVXF3QpVGkcxN7Uvgwey9jjJ31E6vvJMVw3tNrRa8UDrPQsoX6WPYhTeoCowvEdg14i4w"
SIGNED_P2WPKH_PSBT_B64 = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAAiAgLnqyU3tdSelwMJquBunknzbOHJ/rvUTsjg0cygtPnDGUcwRAIgPmX/O0zUfxIfp8mCKEYY24AxR7BW05OU1OxCDv38a6ECIGy92IrFGGw/Lv0kJTHteRd1dlGsJiN089MdhdYWzWqBAQAAAA=="
SIGNED_P2WPKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(SIGNED_P2WPKH_PSBT).to_cbor())

P2SH_P2WPKH_PSBT = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01v\xefk\xf2\xbd\xd0@\xf3\xc1\xd8:\xcc\xb9t9\xf1\xab\xb1\xa5V\xad\x1d\x0fR\x96\x81\xff\xa7\xe8\xca\x94\x8a\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02\x9c=]\x05\x00\x00\x00\x00\x17\xa9\x14%\x1d\xd1\x14W\xa2Y\xc3\xbaG\xe5\xcc\xa3q\x7f\xe4!N\x02\x98\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x143l\xaa\x13\xe0\x8b\x96\x08\n2\xb5\xd8\x18\xd5\x9bJ\xb3\xb3gB\x87\x01\x04\x16\x00\x148\x97\x1fs\x93\x0fl\x14\x1d\x97z\xc4\xfdJr|\x85I5\xb3"\x06\x03\xa1\xaf\x80J\xc1\x08\xa8\xa5\x17\x82\x19\x8c-\x03K(\xbf\x90\xc8\x80?ZS\xf7bv\xfai\xa4\xea\xe7\x7f\x18s\xc5\xda\n1\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x16\x00\x14p\xbe\xb1\xe0JP\t@\xe9\xf3\xab\xaaf\xe1\xa4\x9a\xc5[\x8f5"\x02\x02\xa2\xfc\x89\x96\xc5&"H\xb5\xda\xef\xc5\xa4\xd0\xcd\xcd\x00\xc10G\xd0\xcb\x13\x02\x816\xeac\r\x87Z\x87\x18s\xc5\xda\n1\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
P2SH_P2WPKH_PSBT_B43 = "ISOGTD+S3R8H0DQLFI44D9XVW+NU6FLJ-.-6DZON$.R31OG$AFCWZGO40V:6HQ.DT2C3.CPVM-F+V+GB$A9G:.K3B:KCWPOU8.LZ4SO1D-W/:PCK5Y1.B$HQGWWR1BN8:9J-HXGFVVL1D3R+MTLP/10MGI6AN$1*5ITO3105-C1QBR+LAR5D7VM/1P*KBYJH6P4LH9GCU5DE2*8MP3*YT2K.KDV32OAMNKHV/VGLX9XJ0*B6850S794RVAWR*LEY40SCBLQ.*OR7T$RZ9581/GKU4KYV48LDPURZMDKBEZXRG2SDL4UYGF330F$4*1JCUL5TS+:*X*+E6D::-0L1L63IAMW:*IVLP$YQUV922+G$OJY.INJRHY/A$0.UFB.VD21PM8ED92HKS5TXCAPFS9LT199UMOMBNKM$HE*7*VOJQ*J7JY1PLG188K8IB97211B+AH$4$GDJ750S--S.H45Y4HA4N$PK5S03HS4K"
P2SH_P2WPKH_PSBT_B58 = "W7hsNtPR1YU4YQRATn9QwVubQ3s4aLKhoSpCJQtZuiqGxTQPhu1FB4bqZdtL2MpygirLgext5jZpLSRKGQEhcuiUjg5wvnyP5EP7w1RxkE4Zc5mxDKyEhRH7k3wcSA8TTahF7Rg7r2cWry4c7LySnwoAGtYP1VRwcgMfbYXroHrrKqgdfaKLmMD1M5bCYpU6fMCzcEK5hXQSFaupmhTyAPHiGAczMSmnsoaeZ4cCNpZzexK6FkYES1XTBkroLD68tYejJTjkEpASRVTwS1LUJHEUVmAgASWQ1r3x9yGQaSamXqvedoZ3dNuUsmVJNdGNjKFJRsQugzxEHEj2PWJCpYCUo4Ms79wRkSYjeaQaEEHnBLnkbhPdL6rUu5oGCpzkkgewTcH5hSPA8GefzSgLo3CrGQgY5K3GvPTH5aP6VvMWpUBHGiPqddjQzqeAePxKHi6T"
P2SH_P2WPKH_PSBT_B64 = "cHNidP8BAHICAAAAAXbva/K90EDzwdg6zLl0OfGrsaVWrR0PUpaB/6foypSKAQAAAAD9////Apw9XQUAAAAAF6kUJR3RFFeiWcO6R+XMo3F/5CFOApiHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAAAAAQEgAOH1BQAAAAAXqRQzbKoT4IuWCAoytdgY1ZtKs7NnQocBBBYAFDiXH3OTD2wUHZd6xP1KcnyFSTWzIgYDoa+ASsEIqKUXghmMLQNLKL+QyIA/WlP3Ynb6aaTq538Yc8XaCjEAAIABAACAAAAAgAAAAAAAAAAAAAEAFgAUcL6x4EpQCUDp86uqZuGkmsVbjzUiAgKi/ImWxSYiSLXa78Wk0M3NAMEwR9DLEwKBNupjDYdahxhzxdoKMQAAgAEAAIAAAACAAQAAAAAAAAAAAA=="
P2SH_P2WPKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2SH_P2WPKH_PSBT).to_cbor())

SIGNED_P2SH_P2WPKH_PSBT = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01v\xefk\xf2\xbd\xd0@\xf3\xc1\xd8:\xcc\xb9t9\xf1\xab\xb1\xa5V\xad\x1d\x0fR\x96\x81\xff\xa7\xe8\xca\x94\x8a\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02\x9c=]\x05\x00\x00\x00\x00\x17\xa9\x14%\x1d\xd1\x14W\xa2Y\xc3\xbaG\xe5\xcc\xa3q\x7f\xe4!N\x02\x98\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00"\x02\x03\xa1\xaf\x80J\xc1\x08\xa8\xa5\x17\x82\x19\x8c-\x03K(\xbf\x90\xc8\x80?ZS\xf7bv\xfai\xa4\xea\xe7\x7fG0D\x02 u\x0c\xf8\xe6\x03\x15l\xab\xaa7a`\x1f\xcb\xc5\xd92TC\x97\xbd\xed\xfeS\xeeC\xf4\x1d\xddc\x1cx\x02 4{\xe5K\xe5\xf2F\x04\xd5\x05V\xe8}K\x00\xcc\x93)\x90\x1f\r\x02,\xee?\xd8\xed\xd2\xb8\x97\xcaS\x01\x00\x00\x00'
SIGNED_P2SH_P2WPKH_PSBT_B43 = "31W0038UW96VZD2Q88M9:FYY87X4FB-DLUX80$J+*6M/NA7YI0E702LIMVHP-CBILLLY8E9PHZ3-4UCAWCK3N/5HNYV+SL*NPX1$+3/N-LP7WTNIFF.D9TT4LF9$K$VM4X6X827/5H2YLN.MIML4ZPPGX7G1079T2Q3AH$P*FVWM7M:*RE7+JZFAU7IHH.NRNPPJ/:Z18969$74ED0S2I0W3C:7+WZB1Y+F/GG+5KE9F$:$1G7FI19/V10Q$/S9*PD0PGAA/SQI025O$3R3IS-N/19CLTVJI587I7H7Q.1OB.9AERKA0JMZM3MH4LN77JOKLDB1GR$QX8ST-*756$8IU"
SIGNED_P2SH_P2WPKH_PSBT_B58 = "z1ehfo7UfTTs66xsqudw4HQ9hfvy3QyFp427Cgnzd83AaYzZzV66eRXKHnpVVk2ya4pyhcRK5PcKusFygD3QcBumtRyy1JmTDszD6aBYci4Keixc6ETpCieqhMSGAqjUBd7XhHjbecWS6EcL6yg5h5TummGLDaCXwiMZX4X7EpBV3YmJnTjg23gWqzC7JLDae9KDknBK7V6tZ9x6t9A7dYtWy2Jg7unN61n3xc4k4aGDSuhsh5EgpNSBsWGzCMe9CSniGKBjrw69iJmWa83WCpN5T9Uu86GtYvLYMnJ8SfMMHRjXrgszzy4E4XEjM9"
SIGNED_P2SH_P2WPKH_PSBT_B64 = "cHNidP8BAHICAAAAAXbva/K90EDzwdg6zLl0OfGrsaVWrR0PUpaB/6foypSKAQAAAAD9////Apw9XQUAAAAAF6kUJR3RFFeiWcO6R+XMo3F/5CFOApiHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAAAAIgIDoa+ASsEIqKUXghmMLQNLKL+QyIA/WlP3Ynb6aaTq539HMEQCIHUM+OYDFWyrqjdhYB/LxdkyVEOXve3+U+5D9B3dYxx4AiA0e+VL5fJGBNUFVuh9SwDMkymQHw0CLO4/2O3SuJfKUwEAAAA="
SIGNED_P2SH_P2WPKH_PSBT_UR_PSBT = UR(
    "crypto-psbt", PSBT(SIGNED_P2SH_P2WPKH_PSBT).to_cbor()
)

P2WSH_PSBT = b'psbt\xff\x01\x00\xb2\x02\x00\x00\x00\x02\xadC\x87\x14J\xfae\x07\xe1>\xaeP\xda\x1b\xf1\xb5\x1ag\xb3\x0f\xfb\x8e\x0c[\x8f\x98\xf5\xb3\xb1\xa68Y\x00\x00\x00\x00\x00\xfd\xff\xff\xffig%Y\x0f\xb8\xe4r\xab#N\xeb\xf3\xbf\x04\xd9J\xc0\xba\x94\xf6\xa5\xa4\xf8B\xea\xdb\x9a\xd3c`\xd4\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02@B\x0f\x00\x00\x00\x00\x00"\x00 \xa9\x903\xc3\x86b3>Y\t\xae<=\x03\xbdq\x8d\xb2\x14Y\xfd\xd5P\x1e\xe8\xa0RaMY\xb4\xe2\xd8\xd2!\x01\x00\x00\x00\x00"\x00 \x8d\x02\x85\r\xab\x88^\xc5y\xbbm\xcb\x05\xd6 ;\x05\xf5\x17\x01\x86\xac\xb8\x90}l\xc1\xb4R\x99\xed\xd2\x00\x00\x00\x00O\x01\x045\x87\xcf\x04>b\xdf~\x80\x00\x00\x02A+I\x84\xd5I\xba^\xef\x1c\xa6\xe8\xf3u]\x9a\xe0\x16\xdam\x16ir\xca\x0eQ@6~\xddP\xda\x025\xb8K1\xdc8*|\xfbC\xba:{\x17K\xe9AaA\xe8\x16\xf6r[\xd1%\x12\xb5\xb2\xc4\xa5\xac\x14\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\x9d\xb1\xd0\x00\x80\x00\x00\x02?\xd8\xd7;\xc7\xb8\x8c\xa4\x93Z\xa57\xbf8\x94\xd5\xe2\x88\x9f\xab4\x1ca\x8fJWo\x8f\x19\x18\xc2u\x02h\xc3\rV\x9d#j}\xccW\x1b+\xb1\xd2\xadO\xa9\xf9\xb3R\xa8\t6\xa2\x89\n\x99\xaa#\xdbx\xec\x14&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\xba\xc1H9\x80\x00\x00\x02\x1dO\xbe\xbd\xd9g\xe1\xafqL\t\x97\xd3\x8f\xcfg\x0b\\\xe9\xd3\x01\xc0D\x0b\xbc\xc3\xb6\xa2\x0e\xb7r\x1c\x03V\x8e\xa1\xf3`Q\x91n\xd1\xb6\x90\xc3\x9e\x12\xa8\xe7\x06\x03\xb2\x80\xbd0\xce_(\x1f)\x18\xa5Sc\xaa\x14s\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 \x89\x801pn\xdd\x9e\xb1"g\x85G\x15Q\xce\xa3_\x17\t\xa9o\x85\x96.2\xa0k\xf6~\xc7\x11$\x01\x05iR!\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2!\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87S\xae"\x06\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 3w\xad03\xd1\x05\x9c\xf1\xd25\xbb\x12%\xfc\xa2\xa4\xbf&\xc9R\xd5?o\xef\xc3:-UD\x8d\xc5\x01\x05iR!\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"!\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t!\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01S\xae"\x06\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01iR!\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe!\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v!\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2kS\xae"\x02\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2k\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
P2WSH_PSBT_B43 = "9YO76-S3DRXKI-6JS23**6N$12A3MTF2R66Q0-C-*BD+VB.V3O1EM2VDNMX:*DHL-RMVYZ/.W:9XKN7$4/1M0$$U8+$77KE5:40Z527KZOHA-$MLTL21L3*ON6SCCF:4HMW2K1IS7VUOUF6JW/A+DGMGVF17C0BFK/Y*FDJQWWLX*EEJUR12L3*R0.F6W5674M-+KZUKD+77RB$PGQSTPRX49C25391EP+5/ZJ7$N$F+8*CU24O78HRO0-YO51IO7+A8RZ386S5AK200DG92O6P/QT3W.T$NA7*:GYGTFT+ZC9JWTD-BMVZPBNMT9/EGO.ZHBHAPYHU6MN.U.UZ118L8G4PXR5+*SOXHDQGS$+ZY0HX9X016901VG2$.22I8LNKUGLVRBP.G4Y6DXIAO5B6TPES$F8ALOIDB30SH:29L.*/GSED*V-L0CXWM3SI6YZB59SVDKAJPMCBMDF4:8/Y9FEFIN+5AJ:UQ.J*AC+3N5Y/OOU/HCMOBNRHMN-0QZH8*CQ4-7CSJ7+KU:UX5KFO9XUQG+5U2-2VD6NZCF+N0Y97CP8HR$+N2K98A+0Z8ILV0KI634*/WEI+97-B3E*TW-5F82$N.QRDP/4R9Z6/:0H0$A2DKP2V.RUNDT0E56489TJTX48.1DPCP1KY71RVFFEC:/8:3S6EIS2DETQ2U9.N6TK$6+:H6+UH7KG3ZDW39CLSET-V6MEZSTDL*/A65IK.F3TEJSF++3FOO+-F2SOYFS.V/*SSMCJ7$2Z63SS0K+*O88Y-9+A-IQ04-3VE7PAI$MCR*J6O0$*ZJ9W07:/G+ZVGHJIE:/00UE0*CXLY8COUJIB1ITXR.YNFTLT9B.-IA6KQ7R/56G.54NTU2E657O0KNC0DT$+EGI**JM5F0YNRL01/Y*O:1WQU5J*TTZJGG-HJZA2Q+0F:ML1PY1MXYWNM8ABM4*F33XH6HUZMAW82FRSP302M4NARGWWA2DI8CC1$84B/NFJ5WOJE.5UOUUMUILQJZIK3PA2P-18SQTV*R258MJQ+:++DYHCHI6B5I+J3$OB1AKOLKY4I5XD.3Q2JK*RJ1E1LOU1IV/H7555LHI:RKDV-W995M3-*H4-DBBLDSI9BC*C+U978N2-9K$6+0V/PN-TR.-WIBBBI:3QNPXZ/N4MHI+JI:NIN/80OOG39A9$$G3FE+V71:/Y1VD0UUW.+XTVSO$6SHD:1JXTWYUEAPZUD5/28Z5KW843*BS*2.$WYMG+7YI1.H38BL7YN8/4-34XGFS/L.+V0:RSOAU8NP4ZCAU3Q:GL1/SG5ZU$:*58DIWF8.RNIRG22S18LLNKJXQSY.PH3+66PH0J9*I8S9E70-+*W4ADFYICDA4-0$-MTPE7LO*1*UT/Q6DTUBY0MYTKELTSOGJ0*IFU-N9L3E*8T9/Z:D2JMAI-JJQ7EKP859SIN:+I:Z3G209-DA0$9*H7GBEMOM3V5S/T$LLA/J.U-C5+ZIALSP37NKX2*PWB216D6OITOLQ:3.OAG4U/R45PH$$:K1D/$75QC9SK6S7.O0UJFZK7F*PFY8XJHGP-O.P4E07/M-RKIHQ7L$VFN292+UN8F7KZYP$NF/JY4N+9.RXV1DS**QPYQVY2+U9QR/+1T7-2/YAG9K*T549*:/578Q.AI0/1TQZCCG9FLLL4J$+ETZ0LKF+*3DN84F8GC-P4EYLAF923H9JRXNHXDDPN/NX$O$4SELXX$S8QNZJO$Y7GD/LKH$5:-9J6PMTVT/G3+WS-T*FBFTI3JB/A0OWEPAY:GTOFMBV/M$L1.P$N0S2DL/O4D4SUVJ76S21/:Y$VKF4V+SV-0/UO1GSK:G*H-GGL+ST8MBNG*DUEZHCC-$4J9KRL39V9G00YDA6SW2IF8AKCR9L7YV05RGHEJA0BYZVPYOL:KV/UL+$5ZMHJ9F84Q4YU-XR9THI-/$2W9ZQNR-J-N+WXC+A3FSA$2B4$FQH$71P0T8EBR+WM3W-XT*UG$YKZV3*$HU8Q-XRBXD6Q8K.4$COENY4/V3VL5O7SP.0$5+R5VHO./ULKTKC0G/WG8-5*IXB.4QHRYG90IV48VVNZ2-W*Q0QN7XPJIXK1FNPVQNECX:1$+C.U7*I1.WF.N-UVXNPJZCIOCIFJC1-Z7SWS:3SP7N1OCJK.PB4PVGM*.H6BC8ED4*587E:UD"
P2WSH_PSBT_B58 = "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"
P2WSH_PSBT_B64 = "cHNidP8BALICAAAAAq1DhxRK+mUH4T6uUNob8bUaZ7MP+44MW4+Y9bOxpjhZAAAAAAD9////aWclWQ+45HKrI07r878E2UrAupT2paT4QurbmtNjYNQBAAAAAP3///8CQEIPAAAAAAAiACCpkDPDhmIzPlkJrjw9A71xjbIUWf3VUB7ooFJhTVm04tjSIQEAAAAAIgAgjQKFDauIXsV5u23LBdYgOwX1FwGGrLiQfWzBtFKZ7dIAAAAATwEENYfPBD5i336AAAACQStJhNVJul7vHKbo83VdmuAW2m0WaXLKDlFANn7dUNoCNbhLMdw4Knz7Q7o6exdL6UFhQegW9nJb0SUStbLEpawUAgjLdzAAAIABAACAAAAAgAIAAIBPAQQ1h88EnbHQAIAAAAI/2Nc7x7iMpJNapTe/OJTV4oifqzQcYY9KV2+PGRjCdQJoww1WnSNqfcxXGyux0q1PqfmzUqgJNqKJCpmqI9t47BQmu4PEMAAAgAEAAIAAAACAAgAAgE8BBDWHzwS6wUg5gAAAAh1Pvr3ZZ+GvcUwJl9OPz2cLXOnTAcBEC7zDtqIOt3IcA1aOofNgUZFu0baQw54SqOcGA7KAvTDOXygfKRilU2OqFHPF2gowAACAAQAAgAAAAIACAACAAAEBK4CWmAAAAAAAIgAgiYAxcG7dnrEiZ4VHFVHOo18XCalvhZYuMqBr9n7HESQBBWlSIQJOjQgMfX26XEf+trHIEk3rYkEX5Y2NfrFKQARPcd2X8iEDBWHUgq25PfHvE+hlcBryJG7wo2y8jKUSPY7sd85OOMchA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHU64iBgJOjQgMfX26XEf+trHIEk3rYkEX5Y2NfrFKQARPcd2X8hwmu4PEMAAAgAEAAIAAAACAAgAAgAAAAAABAAAAIgYDBWHUgq25PfHvE+hlcBryJG7wo2y8jKUSPY7sd85OOMccAgjLdzAAAIABAACAAAAAgAIAAIAAAAAAAQAAACIGA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHHHPF2gowAACAAQAAgAAAAIACAACAAAAAAAEAAAAAAQErgJaYAAAAAAAiACAzd60wM9EFnPHSNbsSJfyipL8myVLVP2/vwzotVUSNxQEFaVIhAiKCMRLlzIhLkRbLIUIMx5KYJM0v6LcjW/mS6K7eFGwiIQKDzUflU23LeecRgzDo5IBCEvaWGfHW7JkNxzXvuc7FdCEDC5DtLoa61/Kk/pdpu0F9e6nKoRJIB9v7Ni377rZefgFTriIGAiKCMRLlzIhLkRbLIUIMx5KYJM0v6LcjW/mS6K7eFGwiHAIIy3cwAACAAQAAgAAAAIACAACAAAAAAAAAAAAiBgKDzUflU23LeecRgzDo5IBCEvaWGfHW7JkNxzXvuc7FdBwmu4PEMAAAgAEAAIAAAACAAgAAgAAAAAAAAAAAIgYDC5DtLoa61/Kk/pdpu0F9e6nKoRJIB9v7Ni377rZefgEcc8XaCjAAAIABAACAAAAAgAIAAIAAAAAAAAAAAAABAWlSIQKtIdmtKKuZrH7f2R4iIU8RWVOrCdHVWBCS+0e9pZJy/iEDoH074LrWPIA10hyXtBCJDT06GdLkA6+z/PxoJqomPHYhA6GoQ/otQdk71nUpYZFfbkSKdBkkSj4CuPTPYrzGp6JrU64iAgKtIdmtKKuZrH7f2R4iIU8RWVOrCdHVWBCS+0e9pZJy/hwCCMt3MAAAgAEAAIAAAACAAgAAgAEAAAAAAAAAIgIDoH074LrWPIA10hyXtBCJDT06GdLkA6+z/PxoJqomPHYcc8XaCjAAAIABAACAAAAAgAIAAIABAAAAAAAAACICA6GoQ/otQdk71nUpYZFfbkSKdBkkSj4CuPTPYrzGp6JrHCa7g8QwAACAAQAAgAAAAIACAACAAQAAAAAAAAAAAA=="
P2WSH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2WSH_PSBT).to_cbor())

SIGNED_P2WSH_PSBT = b'psbt\xff\x01\x00\xb2\x02\x00\x00\x00\x02\xadC\x87\x14J\xfae\x07\xe1>\xaeP\xda\x1b\xf1\xb5\x1ag\xb3\x0f\xfb\x8e\x0c[\x8f\x98\xf5\xb3\xb1\xa68Y\x00\x00\x00\x00\x00\xfd\xff\xff\xffig%Y\x0f\xb8\xe4r\xab#N\xeb\xf3\xbf\x04\xd9J\xc0\xba\x94\xf6\xa5\xa4\xf8B\xea\xdb\x9a\xd3c`\xd4\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02@B\x0f\x00\x00\x00\x00\x00"\x00 \xa9\x903\xc3\x86b3>Y\t\xae<=\x03\xbdq\x8d\xb2\x14Y\xfd\xd5P\x1e\xe8\xa0RaMY\xb4\xe2\xd8\xd2!\x01\x00\x00\x00\x00"\x00 \x8d\x02\x85\r\xab\x88^\xc5y\xbbm\xcb\x05\xd6 ;\x05\xf5\x17\x01\x86\xac\xb8\x90}l\xc1\xb4R\x99\xed\xd2\x00\x00\x00\x00\x00"\x02\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87G0D\x02 h?m\x19\x04C\x89\x95\x8b\xba\xed\xbb\xba8)\t\xae^\xe3`\x16G\xc8\x8bq\x9c\x0e\xbc\xc5\xb1j\xa2\x02 \x05\rP(\xe0\x9cc])q\xe5\xe2S\x9f\xaf+\xe4_\xa9\xc6\xf9\r"%\xf4\xa2\x00;\xa2\xaf2W\x01\x00"\x02\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01G0D\x02 ~O\x1b\x8c\xbb\x87x\xa3\xbb\xff\x04\xd8\x10Cq\xc8Y\x0f;N6\x97\xd8S\xfeti\x80\xb3\x12\xe0>\x02 l\x93=\x02m\xb4<\x90\xf4%\xf9Z${\xb7\xecO\x19\x15\xa3\xa3S\xf2Q\x81\xdcX\xfb\xd5&\x9e\xc5\x01\x00\x00\x00'
SIGNED_P2WSH_PSBT_B43 = "R3P$B6$NWMQV566O5L.OASUON8NVGBQI$MY*W$EAZ1OC++PK4FRSTPA0ME9F-LQM9G3GUS95CCWK25VNO51YQ/ACDJEH*8R.KK2D4G5W*Y.A5-PX-*Q461BQC$+3DGF/-XD9VY2A4T7C87L+HLSRE03MMTJ3FNQVZWW5/SU946RUFUQ1+BAO*5I$.I3H*8F7/SPL82GR+C024Q7*/4MT5G2.3RQ-1V7FUPGHP+$$C7N4/3PP5RE*L-NWTRT1AC/K-/MAW6:4WKYBG43X1CM-.0*FIUWY*7DLI.S6A7YA1/E.13+RSVPEVK7Z4HTYH+A$NM3FAMR/S9F:R3Q/GU$-RH34JK6101K2LTC2.KB:FEYBSZZ:3959RPFBW+39/3C4F6.H+-8ZV:QX7W/8XLE9S6R5Q/I3KJ-:M*5X/SAS5QJ*HI+QSN5HL.R34EZOL51NEA10LVY/4/B8/CK/RNCQQE47Y2R/G3T+:N-:1STYSS+MBO+QN*I350QE858LVP0HO$50LFV*Z.9K38L:UP.$..BX/$8KC85E2O56-A604CZ9QW8O$C9Z-+$NJ5W+ZOO5REAI+URGQBBCYX*FVW-A6"
SIGNED_P2WSH_PSBT_B58 = "dxJdhwffFEf35difbWcg8GbzULrTLD1nNU737PfSJvKyrqZV2sgaYe1k39JzHXcvjig3Lv2bKKwZ8FCsr7ngMDmYRYMrGxVNZc7AKRC8cTa6JFufwBketBjU9NMLmenb7B3Aw4EW8HPSVdWx7yQehbVRLB7qaoD3yGhJYTAuovpQX5SR15ZNKJLePmFRtNU4v2KN4kGQR8p8qu4jNatkW77qFMkjanUCdSDxRAW6pidvX9QkvqYR9JQawoRy63Km1WCBZq7R83eu5EndnA3iAkKbahn6vr75tGLRQCT8JV4EHoXv3tbCZBHHyS6SCc1dCLgcNLso1WM6Ak3imTvZ1kLWN5uC33W2LHMHQgochnfqfUfFLh4Z8rmXg1fPMnRjUoyfojnGpijGTkbnXbL9zbZj2FNJkMfZ5TZQyM9SvjTBgaFWx8nhSXvkbyP4Tw5BrJmUKft4F5ySP7zK1w8tg71zgPHxEKkbMXeWrvWAYFAwzzHGVVbRqPJ51SdkBELRAyf5y9nW2HosiwBbRvBYD69zKyywdU95LPxy1C9nw"
SIGNED_P2WSH_PSBT_B64 = "cHNidP8BALICAAAAAq1DhxRK+mUH4T6uUNob8bUaZ7MP+44MW4+Y9bOxpjhZAAAAAAD9////aWclWQ+45HKrI07r878E2UrAupT2paT4QurbmtNjYNQBAAAAAP3///8CQEIPAAAAAAAiACCpkDPDhmIzPlkJrjw9A71xjbIUWf3VUB7ooFJhTVm04tjSIQEAAAAAIgAgjQKFDauIXsV5u23LBdYgOwX1FwGGrLiQfWzBtFKZ7dIAAAAAACICA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHRzBEAiBoP20ZBEOJlYu67bu6OCkJrl7jYBZHyItxnA68xbFqogIgBQ1QKOCcY10pceXiU5+vK+Rfqcb5DSIl9KIAO6KvMlcBACICAwuQ7S6GutfypP6XabtBfXupyqESSAfb+zYt++62Xn4BRzBEAiB+TxuMu4d4o7v/BNgQQ3HIWQ87TjaX2FP+dGmAsxLgPgIgbJM9Am20PJD0JflaJHu37E8ZFaOjU/JRgdxY+9UmnsUBAAAA"
SIGNED_P2WSH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(SIGNED_P2WSH_PSBT).to_cbor())

P2SH_P2WSH_PSBT = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01\x1d\xf4\'\xad\xbd\x8bv?G\xcc(F\x92\xd0\xf4\x95\x1a\xdfZ\xca\xc7#>7.\r\x12\xc9\x9e\xe3\xc1\x96\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02\xdc9]\x05\x00\x00\x00\x00\x17\xa9\x14u!\x12s7Xj\x012N\x85TI|\x93\xf1T\xcd\xcf\xe3\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00O\x01\x045\x87\xcf\x04>b\xdf~\x80\x00\x00\x01\xdd\\H\xf6v\x7f\x04`\x9f\xabE\xd5\xc4b\xeeej\xae\xa5$\x8eL\xa7\xed\xed\xebw$\xc2\xdc\xb4\xe5\x02\xab$\x13O{\x08pA\xa1\x8fa\x18\x9f\xeb\xe5\xda\xc6\x8c\xc5^\xf4\xd7\x9f\xbaT\xdb\x81\xfa}\x1c\xb5\x17\x14\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80O\x01\x045\x87\xcf\x04\x9d\xb1\xd0\x00\x80\x00\x00\x01\xe7\x8e\xbf\x9e\xa8y\xa6\x85N\xb3h\x9c\xc2\x83\x1eMB\xf1\xba\xdbXaovW\x9cV\xe7\xbe\xbfO\xd1\x02\x7f\xe0\xe3"7\xa1\x8b2z~\xce9\xc4\xfbq\xa6%\xe0\xc9\xfb\x9d\x06\xf2\xa2q\xdc\xba\xc5\x11\xf8hs\x14&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80O\x01\x045\x87\xcf\x04\xba\xc1H9\x80\x00\x00\x01\xa7:\xdb\xe2\x87\x84\x87cM\xcb\xfc?~\xbd\xe8\xb1\xfc\x99O\x1e\xc0h`\xcf\x01\xc3\xfe.\xa7\x91\xdd\xb6\x02\xe6**\x99s\xeek:z\xf4|"\x9a[\xdep\xbc\xa5\x9b\xd0K\xbb)\x7fV\x93\xd7\xaa%k\x97m\x14s\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x14\xaf\xde\t\'\xf3\xbd\xf5\xa9\xc3\xdbH;\xb8L\x93\xa5$\x96\x7f>\x87\x01\x04"\x00 \xe7\xa2\x14\x15\xf9\xc7K\xd7\xe8&\x9c\xac\x05\x15\xa2\xfa\xec\xd40\xc2p\xa2R\xe6\xaam\x15-\xec\x8e\x90\xe9\x01\x05iR!\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03!\x03f rK\xb0\x8d\xa8v\xf7\x08\x95F\x00:\xc0\\y\xd7\xee\x9a\xca\xbc\xde\x08\x846xN3\x7f\x13\xed!\x03\xa7RPg\xdbg\'\xd8#\xc2fC\x12#\xa7\x03i\x92\xb6JR\xd5\xdbJ\xd3\xea\x9a\x8c\xa1\x00\x89\xb0S\xae"\x06\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03f rK\xb0\x8d\xa8v\xf7\x08\x95F\x00:\xc0\\y\xd7\xee\x9a\xca\xbc\xde\x08\x846xN3\x7f\x13\xed\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03\xa7RPg\xdbg\'\xd8#\xc2fC\x12#\xa7\x03i\x92\xb6JR\xd5\xdbJ\xd3\xea\x9a\x8c\xa1\x00\x89\xb0\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00"\x00 d\x1c\x13\xabNQ\x92\x9a\x8a\xbf\xa1U\xe8\xb4#\xb8\xcd;B\xfd?m\x87\xd6U\xcfMQ\x03\x85\xbf\x04\x01\x01iR!\x027\xda5Ru8\x1e\xbb\xbf\x98d\xaa\xd6~\x03\x99\xd8\x9f\xcbW~\x9c\xe6\xb0h\x02\x94\xf3\x86\xb3e\x0c!\x02\xfa\x11*\x9bu\xe6F\xdf:\xd8\x01E{"{\xa7Y\xbc\x03\xe5{s8\xfa9\xa8\xd46\x00\x9f\x83\x81!\x03\xf3\x14U\xfcF\x87\x897>\x8d\xcb\x07\xc0\xa61\x1b/ w\x064\xed\x1e\x95H\x04M\xa2\x13d\r\xd4S\xae"\x02\x027\xda5Ru8\x1e\xbb\xbf\x98d\xaa\xd6~\x03\x99\xd8\x9f\xcbW~\x9c\xe6\xb0h\x02\x94\xf3\x86\xb3e\x0c\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x02\xfa\x11*\x9bu\xe6F\xdf:\xd8\x01E{"{\xa7Y\xbc\x03\xe5{s8\xfa9\xa8\xd46\x00\x9f\x83\x81\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xf3\x14U\xfcF\x87\x897>\x8d\xcb\x07\xc0\xa61\x1b/ w\x064\xed\x1e\x95H\x04M\xa2\x13d\r\xd4\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
P2SH_P2WSH_PSBT_B43 = "7ZB23D47D0SL*Y69MFM-Y64LVJD48X$9XZO1J/-L0B.624*OS$T6-RL6--2HB:BJ/CZLFHQ8XWAXNB5UZ91+Y*/SV.4J:VE$J9MMCCOVW$EB6++CJ.X-O8OJ$TSAWI8W38*U:08G+2NKH*CCZRGY0ZABPJ3ESQ6VFNNSDNEYC8KG/QX8R72LXF*4Z+8373D*LLYIOUH+LKJKP5LM+2ZOXD05+G2-H-ZL5N585FA7BF9SYRFRX:U59MND9DEKQ13CKD7+M9TA*3/UP$IIY/9MSQKFLAOQ71UC98XLJ2DP+YP0+-WRV.9CNTV2/X/*1+VQK2:Z0MPT$1H$I:RS1T3.+072$4EWIC:.C0QK4M7JA:HE19Q$9H3U.APAPQN$K7$A6.G6S*K.X2NAAARU5E1-$SOXU3D$$AFF-CF9QMXU4UDF.*7:2DV5P+J$59J8P$4I.FII$FK0U/S6LV$B9.ZG73BC57G77:.03T7B1A1IB6S8-Z:93C$GZO.Q+O/ZSEFG9TRQWACXPPA1KDTTAS4WDT9*/J72B+U52S2ER58Y93VQ4SEQ:X54CW4-8*YXIRZVPV6EOHRE:F.EFUU4LQO+3ZOX706F+GJ2AP+UIEB*XY$*9Z4Q0S3JC1+9J07AA21I3$S8:V0EOY$F$XO/T9PDFY*0D+3YSJW7QVTOT6KID::3F.3:K1-S*243V53H+W.$Y3:C$V8.7GMF7BDZST:7D$C$6AKI3BUVNR2.0Q+BPVC2-I/TUN93WBXM495N8T.7PRSSCZM1M1ZJU.W+G-Z94JK69UVKJI.Q8$WV2MGZENWV26NR14GD83GKE5UTMANK+/X4+CJI*6UI63UEDVN3-FY5R2-B$3JD1SY3+:0ELB/IPL4LM8R$W2*:+.G1PX6X.I-4:CY.TP-Q7XN3.PHRD://U+-LJ6LI9QB477PKMJWT.GS7RC*DLCKE4KW4PL4NP$90:LJHR*5-52JV$DCHL33QBPCQVUO:Z5U+U+XALJ.:AJV+ZBD:JFB+0V:5TZ:GEBFSNTQJOPIGBL6QSG9QLINU3*928744+NWR3NV90670ZN7*V1ET5:A:DUSFHCR64YBKVESO$Q5TYD/QR3$N9Z.ZS09+L*.7UWBVXG63TFA33CNGX0:T+VVTG-Y-H:6Y9OX79R6COJJ:A00PO/8I/UIA2*E+ILV/6/C29QHJL05HINPAJZEMYVZNUVSB5TZT0*GWRMYT*W95M:GO0.NE*/S9EU86IS.M/1DO9DP41HA8-BI.XK6VCPEPX3LAAW*842PZ+8/889ODKLRE2PHP0HY9GB3Q6Y74NYHFI:1XHPGURQ+6YLRLCB5OW9/XLDORE6ZC-AQO++I71AWR0FXHAOF0WCY:JWXONP:L*Y7Z-6I6PSF0V-D87MYD:9W2LS8CU8YCVOT978VUB:6JA:/5U+70JM-I5T+RHHF-3FA+IBPVUBKVZV11.+SN71G7X3:L+RV-79GTG$3QAYAVR2F24/-M0FG2DVJ$4RGHRT55RQHVJ5JVS+H3:0+B1YSX57Y94/Z0-+Z07B4-M0BZREBSGUXZU+IL1C59B5QRAR:6BG9+2J.MIJJ5GJT6*2R1D5Z2.H*$L09W$0KLP4C/HIQ$D8AQS*K8:DGKSISC:LW.BR:JSCV+2EVOFAP.O+WOV6P1DMUQX3LYG/3KXK"
P2SH_P2WSH_PSBT_B58 = "iKPPtgBuDNJvZAkJsisSSKkAar78K5TV6Yt41d6teHVeAnqMdnN9j6cd3vgbKtuVYUFg6QJ6RyqarHnqd6jkYSxZxFPimGq9LG4BDffByiQnRkSzTm9CGVK5XYMP1U5REj1PVebpKoQrgXJyWdjautuAVrpkuAhUm7aHDYj5fYBVzqVRJ8GWpJrY3ZzhMNXLdej9UT3DhBHRf8ATeCZrn5JK3CKSkwTjF7Q97DqwjjSDnx9x8NX5v9UcWJyLnxc9Sj5TJDfBQ2MAjFgCd7fFXBxYbavLnhgfjjzades8wgAVxqMJSSN7tbhQacqu1FxVXLBxZsueHK6e4w2o7z3CGUYqJh53TN3KFENTyRh55HrnsAiBy9Kvnho3E4ey141PToTD3uShXef1s3kKKGhgUtYXmoCMqZshuce3wxjJP6A2Kzn6r9kcEXtNbrXEArnuihJ1bq2dS58Kg55WuwmXLZqMFwXTxj96Ds3hjeG8pJMpBKvUNRuJyPUUKPTtGAHUEsDzVL7kzcBLKdHiG8qPgS5PQHUW7jkik32BrHrDsvHK1t6SBLF8PKpdkZjPo6Pad4p7uS3vyXkV3bvucpjcR2jq4kmj1p5y73cUKFiopBujFRUTfX5dzU96KXZK5tkiWVcUF9hRvmaEfSKwfvVN5B7ThQrZkuMdKoB5VHAie3LrqEyzduJbwcA2ErTGCjArkJxY2YH9KeostknMwNn83C843L38nxqh2UXgd9CGgG57tvPg2BHqBd7pWXfbHCvazHao5i3M1QesrhDvW4tteabJjRQqsEaxiumg8R5J7ByRgxZFBgGQnU6PH8VkNQCVPBWpAdm4XCpccgFsSkbB1VaYJCfXF1qVCDvC9HZ2VfJCKwHvmagZ6hTeoxx1M4nh51tNeJEGSZahTxnWsF49me35MNXBS3agEQ42RACSgDUdPvCveyK2yUqnX5Ka4A5fMznqEZDhFQsfMrude688TKLyqtc4KfVXSDjZgK2xdpt8BsXHM77mA1vynDSkAps9L7qnPwx4UaGimG8XESSHBQSvyxE7U6j3UZiDLtuWeSwJMcjzEUAKuVhAAYAdv6qQkjwueHMPNifpgpoahUqhphExtzxsQujpsNAiYg5U3RqfbWQ77appzjFmGmvKrC8vXyGMzwM11Fve5ac8CKPssfjxeeZ53ufpCdgbLFLd7AVSA3HHhUpiEyuRVnhL5BGtQCvz1MvpbcNYyBwAZ6uRxnhjMmbxTnZ5qiyJEdmssTxZxhV5cYjZtngQun27QffbMqMvB83zrJKcr6SrahWmGabjXULdJVqqqbaY5KWsq5jFBh6B4FMR6zhxYj742d32zHWJWf4PwEQ1HdHZKiQgYrUKE5Rys2XKRSMK9AvYxEcMRTvW2Zhv4uDeDNS1ESsFQcS3ZR1kmZV8ZXzEfQFcXUa5dyjfYyoAXqkJZP8LcdjrUmWjdHezcn1CPJ4pf8zNirSufggFYhRbFkahK4rx9QzD2T4qCT5ygabSqUZHXgqnAxsHmoSD6w4oH7BrH55trHjRChXCVhs4qoU34s"
P2SH_P2WSH_PSBT_B64 = "cHNidP8BAHICAAAAAR30J629i3Y/R8woRpLQ9JUa31rKxyM+Ny4NEsme48GWAAAAAAD9////Atw5XQUAAAAAF6kUdSESczdYagEyToVUSXyT8VTNz+OHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAABPAQQ1h88EPmLffoAAAAHdXEj2dn8EYJ+rRdXEYu5laq6lJI5Mp+3t63ckwty05QKrJBNPewhwQaGPYRif6+XaxozFXvTXn7pU24H6fRy1FxQCCMt3MAAAgAEAAIAAAACAAQAAgE8BBDWHzwSdsdAAgAAAAeeOv56oeaaFTrNonMKDHk1C8brbWGFvdlecVue+v0/RAn/g4yI3oYsyen7OOcT7caYl4Mn7nQbyonHcusUR+GhzFCa7g8QwAACAAQAAgAAAAIABAACATwEENYfPBLrBSDmAAAABpzrb4oeEh2NNy/w/fr3osfyZTx7AaGDPAcP+LqeR3bYC5ioqmXPuazp69HwimlvecLylm9BLuyl/VpPXqiVrl20Uc8XaCjAAAIABAACAAAAAgAEAAIAAAQEgAOH1BQAAAAAXqRSv3gkn8731qcPbSDu4TJOlJJZ/PocBBCIAIOeiFBX5x0vX6CacrAUVovrs1DDCcKJS5qptFS3sjpDpAQVpUiECZ+pFYkOTVjB+eG+vQFA3MNjZWiA6DjRcs1Wl36A/zgMhA2Ygckuwjah29wiVRgA6wFx51+6ayrzeCIQ2eE4zfxPtIQOnUlBn22cn2CPCZkMSI6cDaZK2SlLV20rT6pqMoQCJsFOuIgYCZ+pFYkOTVjB+eG+vQFA3MNjZWiA6DjRcs1Wl36A/zgMcc8XaCjAAAIABAACAAAAAgAEAAIAAAAAAAAAAACIGA2Ygckuwjah29wiVRgA6wFx51+6ayrzeCIQ2eE4zfxPtHCa7g8QwAACAAQAAgAAAAIABAACAAAAAAAAAAAAiBgOnUlBn22cn2CPCZkMSI6cDaZK2SlLV20rT6pqMoQCJsBwCCMt3MAAAgAEAAIAAAACAAQAAgAAAAAAAAAAAAAEAIgAgZBwTq05RkpqKv6FV6LQjuM07Qv0/bYfWVc9NUQOFvwQBAWlSIQI32jVSdTgeu7+YZKrWfgOZ2J/LV36c5rBoApTzhrNlDCEC+hEqm3XmRt862AFFeyJ7p1m8A+V7czj6OajUNgCfg4EhA/MUVfxGh4k3Po3LB8CmMRsvIHcGNO0elUgETaITZA3UU64iAgI32jVSdTgeu7+YZKrWfgOZ2J/LV36c5rBoApTzhrNlDBwCCMt3MAAAgAEAAIAAAACAAQAAgAEAAAAAAAAAIgIC+hEqm3XmRt862AFFeyJ7p1m8A+V7czj6OajUNgCfg4EcJruDxDAAAIABAACAAAAAgAEAAIABAAAAAAAAACICA/MUVfxGh4k3Po3LB8CmMRsvIHcGNO0elUgETaITZA3UHHPF2gowAACAAQAAgAAAAIABAACAAQAAAAAAAAAAAA=="
P2SH_P2WSH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2SH_P2WSH_PSBT).to_cbor())

SIGNED_P2SH_P2WSH_PSBT = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01\x1d\xf4\'\xad\xbd\x8bv?G\xcc(F\x92\xd0\xf4\x95\x1a\xdfZ\xca\xc7#>7.\r\x12\xc9\x9e\xe3\xc1\x96\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02\xdc9]\x05\x00\x00\x00\x00\x17\xa9\x14u!\x12s7Xj\x012N\x85TI|\x93\xf1T\xcd\xcf\xe3\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00"\x02\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03G0D\x02 \x1f\xa0f\x1ct\xd6\xb9S\xbd\xc4"\x0cY\x19\xe0\xe4p\xdc\xe8qR\xc8$\xf4Hf\xa6\x07\x8e\xda\x16b\x02 W;\xfb\xc0\xbaWo]/\xcc\xd8\xdb\xe8\xc85\xee\x9bx\x1c\xea\xba\xf4[vM\xac\xc2\x11\xae-G\xc7\x01\x00\x00\x00'
SIGNED_P2SH_P2WSH_PSBT_B43 = "31W0038UW96VZD2Q88M8T/IZEH66DKKBYZHJR:RY1QZU7/V6N:$EBH$BX-+X*SWV$Q616P8ZN86KB+79YJ.JAY0$C$-$OYSK0:O.A/MBE5GLS:3:L-V4WKGQ53UJQMYY9N7:NF9L+D-/QH7QY3VV$LUR0/Z$BRQ57$GG/CXQ5HQ.XD9L*RCYZY/P*WPYMW9.PYWG:DNEI5-.0:TA6/H-PYQNWWD9MBE-V+2YG$5KVQ2TL1--A3K-PI69ZU35ZN/9*U3V$5ME+U++J6I8S*ELJZ1SNOGHPI8XB3$59N0KN2QHK4$67Z**TBEU7CD9NGM37KTGMWR2AV7SBAOE0*U$NCEQ"
SIGNED_P2SH_P2WSH_PSBT_B58 = "z1ehfo7UfTTs66xsqsXDqobpWUPrn97b8G5VjXyEgcrPZRWf7iqNdo3J9BPyvS5zSfk1NDQfMRPWWjGcUoquTtAJ2A2JsNzDqgDYGp4WNaNPDwMVFGwWf967CCfGmXP7zNcwTrRyKT1bvBzdbA3Vwti4wGDaH2SiuY1Hk56tAPFq3nq5T3fWNv2HEwNYbpqSQbcwo1V4rawM1V5Evc7sFVqXgUG2cHSDi6q3ujzDdL2E5N9ybBX18VsAa29XKRVRJkK6bJrap7ZRhd3dQcTRju34HFbnqjUjG18A225wdnZ1JHNxhttr5fZrdsd5ks"
SIGNED_P2SH_P2WSH_PSBT_B64 = "cHNidP8BAHICAAAAAR30J629i3Y/R8woRpLQ9JUa31rKxyM+Ny4NEsme48GWAAAAAAD9////Atw5XQUAAAAAF6kUdSESczdYagEyToVUSXyT8VTNz+OHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAAAAIgICZ+pFYkOTVjB+eG+vQFA3MNjZWiA6DjRcs1Wl36A/zgNHMEQCIB+gZhx01rlTvcQiDFkZ4ORw3OhxUsgk9EhmpgeO2hZiAiBXO/vAuldvXS/M2NvoyDXum3gc6rr0W3ZNrMIRri1HxwEAAAA="
SIGNED_P2SH_P2WSH_PSBT_UR_PSBT = UR(
    "crypto-psbt", PSBT(SIGNED_P2SH_P2WSH_PSBT).to_cbor()
)

MISSING_GLOBAL_XPUBS_PSBT = "cHNidP8BAFUCAAAAASeaIyOl37UfxF8iD6WLD8E+HjNCeSqF1+Ns1jM7XLw5AAAAAAD/////AaBa6gsAAAAAGXapFP/pwAYQl8w7Y28ssEYPpPxCfStFiKwAAAAAAAEBIJVe6gsAAAAAF6kUY0UgD2jRieGtwN8cTRbqjxTA2+uHIgIDsTQcy6doO2r08SOM1ul+cWfVafrEfx5I1HVBhENVvUZGMEMCIAQktY7/qqaU4VWepck7v9SokGQiQFXN8HC2dxRpRC0HAh9cjrD+plFtYLisszrWTt5g6Hhb+zqpS5m9+GFR25qaAQEEIgAgdx/RitRZZm3Unz1WTj28QvTIR3TjYK2haBao7UiNVoEBBUdSIQOxNBzLp2g7avTxI4zW6X5xZ9Vp+sR/HkjUdUGEQ1W9RiED3lXR4drIBeP4pYwfv5uUwC89uq/hJ/78pJlfJvggg71SriIGA7E0HMunaDtq9PEjjNbpfnFn1Wn6xH8eSNR1QYRDVb1GELSmumcAAACAAAAAgAQAAIAiBgPeVdHh2sgF4/iljB+/m5TALz26r+En/vykmV8m+CCDvRC0prpnAAAAgAAAAIAFAACAAAA="


def test_init_singlekey():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, False, NETWORKS["test"]))
    cases = [
        P2WPKH_PSBT,
        P2WPKH_PSBT_B43,
        P2WPKH_PSBT_B58,
        P2WPKH_PSBT_B64,
        P2WPKH_PSBT_UR_PSBT,
        P2SH_P2WPKH_PSBT,
        P2SH_P2WPKH_PSBT_B43,
        P2SH_P2WPKH_PSBT_B58,
        P2SH_P2WPKH_PSBT_B64,
        P2SH_P2WPKH_PSBT_UR_PSBT,
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case)
        assert isinstance(signer, PSBTSigner)


def test_init_multisig():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, True, NETWORKS["test"]))
    cases = [
        P2WSH_PSBT,
        P2WSH_PSBT_B43,
        P2WSH_PSBT_B58,
        P2WSH_PSBT_B64,
        P2WSH_PSBT_UR_PSBT,
        P2SH_P2WSH_PSBT,
        P2SH_P2WSH_PSBT_B43,
        P2SH_P2WSH_PSBT_B58,
        P2SH_P2WSH_PSBT_B64,
        P2SH_P2WSH_PSBT_UR_PSBT,
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case)
        assert isinstance(signer, PSBTSigner)


def test_init_fails_on_invalid_psbt():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, False, NETWORKS["test"]))

    cases = [
        "thisisnotavalidpsbt",
        UR("unknown-type", bytearray("thisisnotavalidpsbt".encode())),
    ]
    for case in cases:
        with pytest.raises(ValueError):
            PSBTSigner(wallet, case)


def test_sign_singlekey():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, False, NETWORKS["test"]))
    cases = [
        (P2WPKH_PSBT, SIGNED_P2WPKH_PSBT),
        (P2WPKH_PSBT_B43, SIGNED_P2WPKH_PSBT_B43),
        (P2WPKH_PSBT_B58, SIGNED_P2WPKH_PSBT_B58),
        (P2WPKH_PSBT_B64, SIGNED_P2WPKH_PSBT_B64),
        (P2WPKH_PSBT_UR_PSBT, SIGNED_P2WPKH_PSBT_UR_PSBT),
        (P2SH_P2WPKH_PSBT, SIGNED_P2SH_P2WPKH_PSBT),
        (P2SH_P2WPKH_PSBT_B43, SIGNED_P2SH_P2WPKH_PSBT_B43),
        (P2SH_P2WPKH_PSBT_B58, SIGNED_P2SH_P2WPKH_PSBT_B58),
        (P2SH_P2WPKH_PSBT_B64, SIGNED_P2SH_P2WPKH_PSBT_B64),
        (P2SH_P2WPKH_PSBT_UR_PSBT, SIGNED_P2SH_P2WPKH_PSBT_UR_PSBT),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0])
        signed_psbt = signer.sign()
        assert signed_psbt == case[1]


def test_sign_multisig():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, True, NETWORKS["test"]))
    cases = [
        (P2WSH_PSBT, SIGNED_P2WSH_PSBT),
        (P2WSH_PSBT_B43, SIGNED_P2WSH_PSBT_B43),
        (P2WSH_PSBT_B58, SIGNED_P2WSH_PSBT_B58),
        (P2WSH_PSBT_B64, SIGNED_P2WSH_PSBT_B64),
        (P2WSH_PSBT_UR_PSBT, SIGNED_P2WSH_PSBT_UR_PSBT),
        (P2SH_P2WSH_PSBT, SIGNED_P2SH_P2WSH_PSBT),
        (P2SH_P2WSH_PSBT_B43, SIGNED_P2SH_P2WSH_PSBT_B43),
        (P2SH_P2WSH_PSBT_B58, SIGNED_P2SH_P2WSH_PSBT_B58),
        (P2SH_P2WSH_PSBT_B64, SIGNED_P2SH_P2WSH_PSBT_B64),
        (P2SH_P2WSH_PSBT_UR_PSBT, SIGNED_P2SH_P2WSH_PSBT_UR_PSBT),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0])
        signed_psbt = signer.sign()
        assert signed_psbt == case[1]


def test_sign_fails_with_0_sigs_added(mocker):
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, True, NETWORKS["test"]))
    signer = PSBTSigner(wallet, P2WSH_PSBT)
    mocker.patch.object(signer.psbt, "sign_with", mock.MagicMock(return_value=0))

    with pytest.raises(ValueError):
        signer.sign()
    signer.psbt.sign_with.assert_called_with(wallet.key.root)


def test_outputs_singlekey():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, False, NETWORKS["test"]))
    cases = [
        (
            P2WPKH_PSBT,
            [
                "Sending:\n₿0.10,000,000\n\nTo:\ntb1que40al7rsw88ru9z0vr78vqwme4w3ctqj694kx",
                "Fee:\n₿0.00,002,820",
            ],
        ),
        (
            P2SH_P2WPKH_PSBT,
            [
                "Sending:\n₿0.10,000,000\n\nTo:\ntb1que40al7rsw88ru9z0vr78vqwme4w3ctqj694kx",
                "Fee:\n₿0.00,003,300",
            ],
        ),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0])
        outputs = signer.outputs()
        assert outputs == case[1]


def test_outputs_multisig():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, True, NETWORKS["test"]))
    cases = [
        (
            P2WSH_PSBT,
            [
                "Sending:\n₿0.18,993,880\n\nTo:\ntb1q35pg2rdt3p0v27dmdh9st43q8vzl29cps6kt3yradnqmg55eahfqfgn83n",
                "Fee:\n₿0.00,006,120",
            ],
        ),
        (
            P2SH_P2WSH_PSBT,
            [
                "Sending:\n₿0.10,000,000\n\nTo:\ntb1que40al7rsw88ru9z0vr78vqwme4w3ctqj694kx",
                "Fee:\n₿0.00,004,260",
            ],
        ),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0])
        outputs = signer.outputs()
        assert outputs == case[1]


def test_xpubs_fails_with_no_xpubs():
    from krux.psbt import PSBTSigner

    wallet = Wallet(Key(TEST_MNEMONIC, True, NETWORKS["test"]))

    with pytest.raises(ValueError):
        signer = PSBTSigner(wallet, MISSING_GLOBAL_XPUBS_PSBT)
        signer.xpubs()
