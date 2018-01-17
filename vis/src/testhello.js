var Hello = {
    message: 'Hello',
    greeting() {
      return `this.message ${this.getName()}`;
    },
    getName() {
      return 'World';
    }
  };