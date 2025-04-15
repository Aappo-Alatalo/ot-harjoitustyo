```mermaid
classDiagram
class Investment
class PortfolioRepository
class BuyService
class PriceService

    Investment <-- PortfolioRepository
    BuyService --> PortfolioRepository
    BuyService --> PriceService

```
