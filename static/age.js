class CalcAge {
  constructor (bdDate, nowDate) {
    this.bdDate = Date.parse(bdDate);
    this.nowDate = Date.now()
  }
  cAge() {
    let subTotal = (this.bdDate - this.nowDate) / 86400000;
    const age = subTotal / 365.25
    return age

  }
}


const t = new CalcAge("1982-5-22", "2024-5-3")
console.log(t.cAge())


//const btn = document.querySelector("")
