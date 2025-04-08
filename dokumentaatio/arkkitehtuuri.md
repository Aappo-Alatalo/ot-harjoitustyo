```mermaid
classDiagram
class Investment
class PortfolioRepository
class BuyService
class PriceService
class yfinance

    Investment <-- PortfolioRepository
    BuyService <-- PortfolioRepository
    BuyService <-- PriceService
    PriceService <-- yfinance

```
