const Money = require('./money')

class Portfolio{
    constructor(){
        this.moneys = [];
    }

    add(...moneys){
        this.moneys = this.moneys.concat(moneys)
    }

    convert(money, currency){
        let exchageRates = new Map();
        exchageRates.set('EUR->USD', 1.2);
        exchageRates.set('USD->KRW', 1100);

        if (money.currency === currency) {
            return money.amount
        }
        let key = money.currency + '->' + currency;
        return money.amount * exchageRates.get(key);
    }

    evaluate(currency){
        let total = this.moneys.reduce( (sum, money) => {
            return sum + this.convert(money, currency);
        }, 0)
        return new Money(total, currency)
    }
}

module.exports = Portfolio;