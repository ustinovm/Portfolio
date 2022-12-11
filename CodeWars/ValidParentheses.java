//This is a naive and simple way of solving the ValidParentheses Kata
//https://www.codewars.com/kata/52774a314c2333f0a7000688
public class Solution{
  
  public static boolean validParentheses(String parens){
    int counter = 0;
    char[] ch = parens.toCharArray();
    for (char s : ch){
      if(s=='('){
        counter +=1;
      }if(s==')'){
        counter -=1;
      }
      if(counter<0){
        return false;
      }
    }
    if (counter==0){
      return true;
    }else{
      return false;
    }
  }
}
