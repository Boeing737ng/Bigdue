describe('Hello', ()=> { 
    describe('greeting', ()=>{
      it('인사 문자열을 반환한다', ()=> {
        const expectedStr = Hello.message,
              actualStr = Hello.greeting();
  
        expect(actualStr).toBe(expectedStr);
      })
    })
  });