# Crypto and on-chain analytics

[Back to the index](../README.md)

## In short

Crypto data is public by design, which makes it a good place to practice reading raw data instead of headlines. This page is about analysis and tooling, not investment advice.

- **Go to the source:** block explorers (mempool.space for Bitcoin, Etherscan for Ethereum, Blockchair for many chains) show every transaction.
- **On-chain metrics:** LookIntoBitcoin and Glassnode turn chain data into cycle indicators such as MVRV; learn what each measures before trusting a chart.
- **DeFi and layer 2:** DefiLlama tracks value locked, fees and yields; L2BEAT rates layer-2 networks by risk, not only by size.
- **Market data:** CoinMarketCap, CoinGecko and TradingView for prices; CoinGlass for derivatives (funding, open interest, liquidations).
- **Build your own:** CoinGecko and BlockCypher APIs, OpenBB as an open-source research terminal.
- **Sentiment indexes** (Fear and Greed, altcoin season) are fun but noisy.

**Where to start:** mempool.space, DefiLlama, L2BEAT.

## Contents

- [Market data and charts](#market-data-and-charts)
- [Block explorers](#block-explorers)
- [On-chain analytics](#on-chain-analytics)
- [DeFi and layer 2](#defi-and-layer-2)
- [Trading tools](#trading-tools)
- [APIs and docs](#apis-and-docs)
- [Learning](#learning)

## Market data and charts

- [CoinMarketCap](https://coinmarketcap.com/pl) ⭐ - Cryptocurrency market data site with prices, charts and market capitalization rankings.
- [CoinGecko](https://www.coingecko.com/) - Crypto market data site with prices, market caps and a free API.
- [CoinGlass](https://www.coinglass.com/) - Derivatives and market data dashboard covering open interest, funding rates and liquidations.
- [Crypto Fear & Greed Index](https://alternative.me/crypto/fear-and-greed-index) - Daily index measuring crypto market sentiment from extreme fear to extreme greed.
- [GeckoTerminal](https://geckoterminal.com/) - Price charts and pool data for tokens across many decentralized exchange networks.
- [TradingView](https://www.tradingview.com/) - Web charting platform and social network for traders covering stocks, crypto and forex.
- [Altcoin Season Index](https://www.blockchaincenter.net/altcoin-season-index) - Index estimating whether altcoins are outperforming Bitcoin, the so-called altseason.
- [Alternative.me Crypto Dashboard](https://alternative.me/crypto) - Overview of crypto prices and Bitcoin analytics on one page, with a free API.
- [Bitcoin Rainbow Chart](https://www.blockchaincenter.net/bitcoin-rainbow-chart) - Live logarithmic growth-curve chart with Bitcoin price bands.
- [Bitcoin Visuals](https://bitcoinvisuals.com/) - Historical and current Bitcoin price, Lightning and node charts and statistics.
- [Bitcoinity.org](http://bitcoinity.org/) - Bitcoin market data charts covering exchange volumes, prices and order books.
- [BitInfoCharts](https://bitinfocharts.com/) - Price, reward, difficulty and hashrate stats for Bitcoin, Ethereum, Dogecoin and Litecoin.
- [COIN360](https://coin360.com/) - Live cryptocurrency price heatmap with market caps, volumes and news.
- [CoinGlass funding rates](https://www.coinglass.com/FundingRate) - Funding rates across perpetual swap exchanges, with comparison views.
- [CoinGlass long/short ratio](https://www.coinglass.com/LongShortRatio) - Long and short ratio data for futures markets across major exchanges.
- [CoinMarketCal](https://coinmarketcal.com/en) - Cryptocurrency events calendar listing project updates, launches and other coin events.
- [Crypto Bubbles](https://cryptobubbles.net/) - Interactive bubble chart visualizing cryptocurrency market caps and price changes.
- [CryptoCompare](https://www.cryptocompare.com/) - Cryptocurrency prices, charts, portfolio tracking and news.
- [Datamish](https://datamish.com/) - Charts of Bitcoin long and short positions on Bitfinex for sentiment and margin analysis.
- [DEX Screener](https://dexscreener.com/) - Real-time charts and trading data for tokens on decentralized exchanges.
- [Investing.com](https://www.investing.com/) - Financial markets site with quotes, charts, economic calendars and news.
- [Maximus Data](https://maxdata.app/charts) - Crypto charting service with market data charts.
- [StockWatch.pl](https://www.stockwatch.pl/) - Polish stock market portal with quotes, company data, dividends and analyses.
- [Withdrawal Fees](https://withdrawalfees.com/) - Comparison of cryptocurrency withdrawal fees across exchanges.

## Block explorers

- [Etherscan](https://etherscan.io/) ⭐ - Ethereum blockchain explorer for transactions, addresses, tokens and gas data.
- [mempool.space](https://mempool.space/pl) ⭐ - Open-source Bitcoin block explorer and mempool monitor with fee and network data.
- [Blockstream Esplora](https://github.com/Blockstream/esplora) - Open-source block explorer for Bitcoin and Liquid, the code behind blockstream.info.
- [Blockstream.info](https://www.blockstream.info/) - Open-source block explorer for Bitcoin, Testnet and Liquid with privacy-friendly access.
- [mempool (GitHub)](https://github.com/mempool) - GitHub organization of the open-source mempool project behind mempool.space.
- [BitInfoCharts Explorer](https://bitinfocharts.com/bitcoin/explorer) - Bitcoin block explorer from BitInfoCharts.
- [Blockchain.com](https://www.blockchain.com/) - Blockchain explorer, wallet and crypto data company site covering Bitcoin and Ethereum.
- [Blockchair](https://blockchair.com/) - Universal blockchain explorer and search engine covering several chains.
- [BlockCypher explorer](https://github.com/blockcypher/explorer) - Open-source block explorer built on top of the BlockCypher API.
- [Blockonomics](https://www.blockonomics.co/) - Bitcoin block explorer and wallet lookup with xPub balance monitoring and no signup.
- [Ethplorer](https://ethplorer.io/) - Explorer for Ethereum tokens, with token prices, charts and analytics.
- [Helium Explorer](https://explorer.helium.com/) - Blockchain explorer for the Helium network.
- [TRONSCAN](https://tronscan.org/) - Block explorer for the TRON blockchain.
- [WalletExplorer](https://www.walletexplorer.com/) - Bitcoin block explorer that groups addresses into wallets.

## On-chain analytics

- [Glassnode](https://glassnode.com/) - On-chain market intelligence platform with Bitcoin and crypto metrics and research.
- [LookIntoBitcoin](https://www.lookintobitcoin.com/charts) - Live Bitcoin on-chain charts and market cycle indicators such as MVRV and NUPL.
- [Artemis Sheets](https://www.artemis.xyz/sheets) - Spreadsheet-based research data for crypto assets and public equities.
- [Blockchain.com charts](https://www.blockchain.com/charts) - Bitcoin and blockchain charts covering network, market and transaction data.
- [CBBI](https://colintalkscrypto.com/cbbi) - Bitcoin Bull Run Index that combines several metrics to estimate the current cycle position.
- [CertiK Leaderboard](https://www.certik.com/) - Leaderboard and audit data from CertiK, a Web3 security auditing firm.
- [CryptoFees.info](https://cryptofees.info/) - Ranking of crypto protocols by the fees users actually pay on-chain.
- [CryptoQuant](https://cryptoquant.com/asset/btc/summary) - On-chain and exchange analytics platform for Bitcoin and other crypto assets.
- [Is This Coin A Scam?](https://isthiscoinascam.com/) - Tool that rates cryptocurrencies for scam risk using contract, holder and audit data.
- [Messari](https://messari.io/) - Crypto research, data and tools platform for analysts and investors.
- [miningpool.observer](https://miningpool.observer/) - Dashboard showing how Bitcoin mining pools select transactions for their blocks.
- [ultrasound.money](https://ultrasound.money/) - Live tracker of Ethereum burned fees and ETH supply.
- [Whale Alert](https://whale-alert.io/) - Tracker of large crypto transactions with market data and alerts.
- [Woobull Charts](http://charts.woobull.com/) - Bitcoin price model and on-chain valuation charts for investors.

## DeFi and layer 2

- [DefiLlama](https://defillama.com/) ⭐ - DeFi dashboard tracking total value locked, fees and yields across protocols and chains.
- [L2BEAT](https://l2beat.com/scaling/tvl) ⭐ - Tracker of Ethereum layer-2 networks showing value secured, risk and security status.
- [MetaMask](https://metamask.io/) - Self-custody crypto wallet and browser extension for Ethereum and other chains.
- [Avalanche](https://www.avax.network/) - Layer-1 blockchain platform for building apps and financial systems.
- [Cardano](https://cardano.org/) - Proof-of-stake blockchain platform developed through peer-reviewed research.
- [Chia Network (GitHub)](https://github.com/Chia-Network) - GitHub organization of Chia Network, the blockchain project built on Chialisp.
- [Compound](https://compound.finance/) - DeFi lending protocol connecting suppliers and borrowers.
- [Hedera](https://hedera.com/) - Public distributed ledger network for decentralized apps and tokens.
- [Ledger](https://www.ledger.com/) - Maker of hardware wallets for storing crypto assets offline.
- [Polygon](https://polygon.technology/) - Ethereum scaling network and stablecoin payments stack.

## Trading tools

- [Bookmap Web](https://web.bookmap.com/) - Web version of Bookmap, showing market liquidity and order book heatmaps.
- [Finviz](https://finviz.com/) - Stock screener and market heatmaps for investors and traders.
- [Gekko](https://github.com/askmike/gekko) - Trading bot and backtester for Bitcoin and other markets, written in Node.js.
- [Hyblock Capital](https://hyblockcapital.com/) - Crypto derivatives analytics with liquidation heatmaps, screeners and backtesters.
- [ichimoku (R package)](https://github.com/shikokuchuo/ichimoku) - R package with visualization and tools for Ichimoku Kinko Hyo trading strategies.
- [OpenBB](https://openbb.co/) - Open-source investment research platform connecting financial data sources with AI tools.
- [The Kingfisher](https://thekingfisher.io/) - Estimated liquidation zones and alerts for crypto futures, for position risk planning.
- [TraderEdge](https://www.traderedge.app/) - Backtesting and trading journal software for forex, crypto and stocks.
- [TradingView-API](https://github.com/Mathieu2301/TradingView-API) - Unofficial Node.js client for real-time market data from TradingView.

## APIs and docs

- [CoinGecko API documentation](https://www.coingecko.com/pl/api/documentation) - Documentation for the CoinGecko crypto market data API.
- [Blockchain.com (GitHub)](https://github.com/blockchain) - GitHub organization of Blockchain.com with its public repositories.
- [BlockCypher](https://www.blockcypher.com/) - Blockchain web services and APIs for several cryptocurrencies.
- [BlockCypher API docs](https://www.blockcypher.com/dev/bitcoin) - Developer API for querying Bitcoin, Ethereum and other blockchains.
- [ethereum.org: Java developers](https://ethereum.org/en/developers/docs/programming-languages/java) - Ethereum.org guide to developing on Ethereum with Java-based libraries and tools.
- [Polygon.io (now Massive)](https://polygon.io/) - Stock market data API with REST and WebSocket access and a free tier.

## Learning

- [Binance Academy](https://academy.binance.com/pl) - Educational hub on blockchain and crypto basics published by Binance.
- [Glassnode Academy](https://academy.glassnode.com/) - Learning resources on on-chain market analytics, now served from Glassnode docs.
