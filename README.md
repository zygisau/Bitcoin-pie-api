# Bitcoin-pie-api

![version][version-badge]  

![Bitcoin Pie]( https://cryptobriefing.com/wp-content/uploads/2019/02/bitcoin-pie.jpg )

University exercise where we had to use bitcoin lib for python to extract different information



## What it does?

This *python powered* console application can do two things.

### Calculate transaction fee 🥧

Every valid bitcoin transaction has its fee. Due to the architecture of transactions, their fees calculation isn't as trivial as it could sound like.

In order to calculate fee, You have to run python file as this:

``` bash
$ python main.py calcfee [txid]
```

Where **calcfee** is specific command that initiates calculation and **[txid]** is transaction's id whose fee You need to calculate. 

### Validate Block 🥧

This application is also capable to validate already generated block by rehashing header parameters.

To validate block, program must be run as:

```bash
$ python main.py validateblock [blockid]
```

Where **validateblock** is specific command that initiates validation and **[blockid]** is spicific block's id.

##  **Prerequisites** 

🥧 Python 3

🥧 Full blockchain node

🥧 Test data which can be found in [here]( https://www.blockchain.com/explorer )



### [v0.1](https://github.com/zygisau/Bitcoin-pie-api/releases/tag/0.1) - (2019-11-29)  

**Added**  

 - Transaction fee and block validation functionality

 - Created README file

   

[version-badge]: https://img.shields.io/badge/version-0.1-orange.svg
