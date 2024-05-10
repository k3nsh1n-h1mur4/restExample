// Obtener Dato del formulario
const form = document.getElementById("form-regh")
//const valueField = form.f_nac.value;
console.log(form.edad)


const btn = document.querySelector("#btn-age")
btn.addEventListener('click', (e) => {
    e.preventDefault();
    let valueField = form.f_nac.value;
    const a = new CalcAge(valueField, Date.now())
    let currentAge = a.cAge()
    console.log(currentAge)
    form.edad.value = Math.abs(currentAge);
})



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
  
  


        









/*const form = document.querySelector('.form-regh')
form.addEventListener('click', (e) => {
    e.preventDefault();
    const d = form.f_nac.value;
    let birthDayToMillis = Date.parse(d)
    let nowToMillis = Date.now()
    let subT = (birthDayToMillis - nowToMillis) / 86400000;
    const age = subT / 365.25;
})*/