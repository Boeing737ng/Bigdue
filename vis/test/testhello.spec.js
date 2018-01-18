describe('Hello모듈의', ()=> { 
  describe('greeting함수는', ()=>{
    it('getName 함수을 호출한다', ()=> {
      spyOn(Hello, 'getName');
      Hello.greeting();
      expect(Hello.getName).toHaveBeenCalled();
    })
  })
});