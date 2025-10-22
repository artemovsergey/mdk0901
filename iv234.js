import Student from './student.js'

export default class IV234 extends Student {

  static Owner = "Офицеркина Татьяна Сергеевна"

  static getOwner(){
    return this.Owner
  }

  constructor(name, age, status) {
    
    super(status);

    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log("Привет мир ...");
  }

  sleep(number) {
    console.log(`Я спал ${number} часов`);
  }
}