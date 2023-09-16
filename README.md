# BTCelParse
[![GNU LGPLv3 license](https://img.shields.io/badge/license-LGPLv3-blue.svg)](https://github.com/Celshade/CelSwap/blob/master/LICENSE.LESSER)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-green.svg)](https://www.python.org/)

_A simple P/L parser for Ordinals on Bitcoin_

This program may be run as a stand-alone CLI tool or integrated into other programs.

<gif>

***

## System Requirements:
_This program was created on WSL2 and is intended for use with Linux/Unix compatible systems._
_Windows OS functionality has not yet been tested prior to release, and additional configuration may be necessary._

1. **Python [3.11+]**:
    * See docs and install instructions -> [here](https://www.python.org/)
    * _This program may work with older versions of python, but this has not been explicitly tested._
        * _Type annotations may break backwards compatibility - modify the program by using the built-in `Typing` module or by removing annotations if using older versions of python._

## Python Requirements:
1. **requests**: Installable via `pip install requests` [->PYPI docs<-](https://pypi.org/project/requests/)

***

## Program Configuration
No additional configuration is needed to run the program as a stand-alone CLI tool.
***

## Running BTCelParse
Simply run the program, and [when prompted] input the **ordinal wallet address** that you wish to parse. \
_You may also provide an [optional] API key from MagicEden if you wish to do so._

To call the program, simply navigate to the program's root directory, and call the program.

i.e.

`python src/ord_parser.py`
***

## Potential Hickups (Rate-Limits)
_Providing an [optional] API key from MagicEden will bypass their rate-limitations; however, you may run the program without one._
_The author of original software [Celshade] is not liable for any blocked IP addresses or negative reprecutions resulting from abusing rate-limits._

Some data sources (i.e. marketplaces, mempool, etc) may specify their own rate-limits. \
The user is responsible for researching and understanding these rate-limits and the consequences for abusing them.
