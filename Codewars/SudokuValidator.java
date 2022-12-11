// Solution to a CodeWars Kata: 
// https://www.codewars.com/kata/529bf0e9bdf7657179000008
import java.util.*;
public class SudokuValidator {
  
  public static boolean checkBlock(int[][] board, int xstart, int xstop, int ystart, int ystop){
    List<Integer> list = new ArrayList<Integer>();
    
    for (int x = xstart; x<=xstop; x++){
      for (int y = ystart; y<=ystop; y++){
        if(board[y][x]==0){
          return false;
        }
        if(list.contains(board[y][x])){
          return false;
        }else{
          list.add(board[y][x]);
        }
      }
    }
    return true;
  }
  
  public static boolean checkVert(int[][]board, int x){
    List<Integer> list = new ArrayList<Integer>();

    for (int y=0; y<9;y++){
      if (board[y][x]==0){
        return false;
        }
      if(list.contains(board[y][x])){
          return false;
        }else{
          list.add(board[y][x]);
        }
      }
    return true;
  }
  
  public static boolean checkHori(int[][]board, int y){
    List<Integer> list = new ArrayList<Integer>();

    for (int x=0; x<9;x++){
      if (board[y][x]==0){
        return false;
        }
      if(list.contains(board[y][x])){
          return false;
        }else{
          list.add(board[y][x]);
        }
      }
    return true;
  }
  
    public static boolean check(int[][] sudoku) {
      for (int x = 0; x<9;x++){
          if(checkVert(sudoku,x)==true){
            continue;
          }else{
            return false;
          }
        }
      for (int y=0; y<9; y++){
        if(checkHori(sudoku,y)==true){
          continue;
        }else{
          return false;
        }
      }
      for (int i =0; i<9; i+=3){
        for (int j=0; j<9; j+=3){
         if(checkBlock(sudoku,i,i+2,j,j+2)==true){
           continue;
         }else{
           return false;
         } 
        }
        }
      return true;
    }
}
