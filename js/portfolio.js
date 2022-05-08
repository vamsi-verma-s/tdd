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
        let rate = exchageRates.get(key)
        if (rate === undefined){
            return undefined
        }
        return money.amount * rate;
    }

    evaluate(currency){
        let failures = [];
        let total = this.moneys.reduce( (sum, money) => {
            let convertedAmount = this.convert(money, currency)
            if (convertedAmount === undefined){
                failures.push(money.currency + '->' + currency)
            } else {
                return sum + convertedAmount
            }
        }, 0)
        if (!failures.length) {
            return new Money(total, currency)
        }
        throw new Error("Missing exchange rate(s):[" + failures.join() + "]");
    }
}

module.exports = Portfolio;