# BTCelParse
[![GNU LGPLv3 license](https://img.shields.io/badge/license-LGPLv3-blue.svg)](https://github.com/Celshade/CelSwap/blob/master/LICENSE.LESSER)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-green.svg)](https://www.python.org/)

_A simple P/L parser for bitcoin ordinals_

BTCelParse is a program designed to help calculate profit/loss for bitcoin ordinals. \
Data parsed and presented by this program is not guaranteed to be 100% accurate.

This program may be run as a stand-alone CLI tool or integrated into other programs.

![](btcelparse_demo.gif)

***

## System Requirements
_This program was created on WSL2 and is intended for use with Linux/Unix compatible systems._
_Windows OS functionality has not yet been tested prior to release, and additional configuration may be necessary._

1. **Python [3.11+]**:
    * See docs and install instructions -> [here](https://www.python.org/)
    * _This program may work with older versions of python, but this has not been explicitly tested._
        * _Type annotations may break backwards compatibility - modify the program by using the built-in `Typing` module or by removing annotations if using older versions of python._

## Python Requirements
1. **requests**: Installable via `pip install requests` [->PYPI docs<-](https://pypi.org/project/requests/)

***

## Program Configuration
No additional configuration is needed to run the program as a stand-alone CLI tool; however, it is **_highly_** recommended that you use an Ordinal API key from MagicEden.
***

## Running the Program
Simply run the program, and [when prompted] input the **ordinal wallet address** that you wish to parse.

_You may also provide an [optional] Ordinal API key from MagicEden if you wish to do so._ \
_If you do not provide an [optional] Ordinal API key from MagicEden, the program may terminate early due to rate-limits_

To call the program, simply navigate to the program's root directory, and call the program.

i.e.

`python src/ord_parser.py`

## CLI Definitions
CLI output has several categories:
* `Total confirmed flips`: Verified purchase/sale prices
    * Includes mints/purchases via official marketplaces using the same wallet (Xverse support via ME)
* `Total confirmed buys`: Verified buys
    * Does not currently include xfers/airdrops/OTC from another source, as these cannot be verified
        * Multi-wallet support will help address some of this (future release)
* `Total confirmed sales`: Verified sales
* `Total confirmed P/L`: Aggregated P/L from confirmed buys/sells
* `Total unconfirmed P/L`: Aggregated P/L from confirmed sells and unconfirmed buys
* `Total potential P/L`: Aggregated P/L from all sources
***

## Rate-Limits and API Keys
_Providing an [optional] Ordinal API key from MagicEden will bypass their rate-limitations; however, you may try to run the program without one._
_The author of original software [Celshade] is not liable for any blocked IP addresses or negative reprecutions resulting from abusing rate-limits._

Some data sources (i.e. marketplaces, mempool, etc) may specify their own rate-limits. \
The user is responsible for researching and understanding these rate-limits and the consequences for abusing them.

ME Ordinal API Rate Limiting: [-> ME Rate limit docs <-](https://docs.magiceden.io/reference/ordinals-api-keys)