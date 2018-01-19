/**
 * Hello test
 * @type {{message: string, greeting: (()), getName: (())}}
 */
var Hello = {
    message: 'Hello',
    greeting() {
      return `this.message ${this.getName()}`;
    },
    getName() {
      return 'World';
    }
  };

/**
 * helloWorld test
 * @returns {string}
 */
function helloWorld(){
    return "Hello world!";
}