// Return the product of consecutive Fibonacci numbers
// this solution was optimized for the codewars server, magic arbitrary numbers were chosen to prevent the server from killing the task
// https://www.codewars.com/kata/5541f58a944b85ce6d00006a
public class ProdFib { // must be public for codewars	
  
	public static long nthFibonacciTerm(int n) {
  //this returns the nth fibonacci term in fixed time
  
    double squareRootOf5 = Math.sqrt(5);
    double phi = (1 + squareRootOf5)/2;
    long nthTerm = (long) ((Math.pow(phi, n) - Math.pow(-phi, -n))/squareRootOf5);
    return nthTerm;
    }
  
	public static long[] productFib(long prod) {
    //this returns the product
    if(prod<14000000){
      
    
    if(prod==1){
      long[] res = {1,1,1};
      return res;
    }
    
    int n0 = 0, n1 = 1;
    int tempNthTerm;
      
    for (int i = 2; i <= prod; i++) {
        tempNthTerm = n0 + n1;
        n0 = n1;
        n1 = tempNthTerm;
      
      if(n0*n1>=prod){
        if(n0*n1==prod){
          long[] res = {n0 , n1 , 1};
          return res;
        }
        if(n0*n1>prod){
          long[] res = {n0,n1,0};
          return res;
        }
      }
      }
    }else{
      for (int i=16;i<prod;i++){
      long one = nthFibonacciTerm(i);
      long two = nthFibonacciTerm(i+1);
      
      if(one*two>=prod){
        if(one*two==prod){
          long[] res = {one , two , 1};
          return res;
        }
        if(one*two>prod){
          long[] res = {one,two,0};
          return res;
        }
      }
    }
    }
    
    long[] res = {-1,-1,0};
    return res;
    
   }
}
