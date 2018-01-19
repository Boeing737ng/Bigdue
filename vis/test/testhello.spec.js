/**
 *  Hello 모듈의 테스트 코드
 */
describe('Hello모듈의', ()=> {
  describe('greeting함수는', ()=>{
    it('getName 함수을 호출한다', ()=> {
      spyOn(Hello, 'getName');
      Hello.greeting();
      expect(Hello.getName).toHaveBeenCalled();
    })
  })
});

/**
 * "Hello world"가 정확히 일치하는지 확인하는 테스트함수
 */
describe("Hello world", function() {
    it("says hello", function() {
        expect(helloWorld()).toEqual("Hello world!");
    });
});

/**
 *  "world"가 포함되어 있는지 확인하는 테스트 함수
 */
describe("Hello world", function() {
    it("says world", function() {
        expect(helloWorld()).toContain("world");
    });
});