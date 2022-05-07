const assert = require('assert');

class Money {
    constructor(amount, currency){
        this.amount = amount;
        this.currency = currency
    }

    times(multiplier){
        return new Money(this.amount * multiplier, this.currency);
    }

    divide(divisor){
        return new Money(this.amount/divisor, this.currency);
    }
}

let fiver = new Money(5, 'USD');
let tenner = new Money(10, 'USD');
assert.deepStrictEqual(fiver.times(2), tenner);

let tenEuros = new Money(10, 'EUR');
let twentyEuros = tenEuros.times(2);
assert.deepStrictEqual(tenEuros.times(2), twentyEuros);


let originalMoney = new Money(4002, 'KWR');
let moneyAfterDivision = originalMoney.divide(4);
let expectmoneyAfterDivison = new Money(1000.5, 'KWR')
assert.deepStrictEqual(moneyAfterDivision, expectmoneyAfterDivison);