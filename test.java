package com.ssafy.b_array;
import java.util.Arrays;
public class ArrayTest_22 {
    private static int R = 4, C = 5;
    private static char[][] map;
    // TODO: deltas 계열의 변수를 초기화 하시오.
    private static int[] dx= {-1,0,1,0};
    private static int[] dy= {0,1,0,-1};
    private static char[] vowel= {'A','E','I','O','U'};
    // END

    private static void setup() {
        map = new char[R][C];
        char alpha = 'A';
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                map[r][c] = alpha++;
            }
        }
    }

    public static void main(String[] args) {
        setup();
//        checkCross();
//        checkX();
//        straight();
        moveHorse();
    }

    private static void checkCross() {
        int sum = 0;
        // TODO: 자음의주변을 +로 탐색하고 요소의 합을 출력하시오.A=0, B=1,..
        
        // END
        System.out.println(sum == 498);
    }

    private static void checkX() {
        int sum = 0;
        // TODO: 모음의 주변을 X로 탐색하고 요소의 합을 출력하시오.(A=0, B=1, ...)

        // END
        System.out.println(sum == 72);
    }

	private static void straight() {
        int sum = 0;
        // TODO: 'K'의 사방으로 영역 내에서 모음을 만나기 전까지 모든 자음들을 합해서 출력하세요.('A'=0, 'B'=1, ...)
        for(int x=0;x<R;x++) {
        	for(int y=0;y<C;y++) {
        		if(map[x][y]=='K') {
        			for(int i=0;i<4;i++) {
        	        	if(map[x+dx[i]][y+dy[i]]!='A'||map[x+dx[i]][y+dy[i]]!='E'||map[x+dx[i]][y+dy[i]]!='I'||map[x+dx[i]][y+dy[i]]!='O'||map[x+dx[i]][y+dy[i]]!='U') break;
        	        	else {
        	        		sum+=map[x+dx[i]][y+dy[i]]-'A';
        	        	}
        	        }
        		}
        	}
        }
        
        System.out.println(sum == 56);
    }

    private static void moveHorse() {
        char maxChar = 'A';
        int maxSum = 0;
        int[] dx_h= {-2,-2,2,2,-1,1,-1,1};
        int[] dy_h= {-1,1,1,-1,2,2,-2,-2};
        // TODO: 모음에서 장기의 말(馬)이동 했을 때 만나는 지점의 합이 가장 큰 알파벳과 그때의 합은? 합이 같다면 큰 알파벳
        
        for(int i=0;i<R;i++) {
        	for(int j=0;j<C;j++) {
        		if(map[i][j]=='A'||map[i][j]=='E'||map[i][j]=='I'||map[i][j]=='O'||map[i][j]=='U') {
        			for(int k=0;k<8;k++) {
        				try {
        					System.out.println(map[i][j]+" >> "+map[i+dx_h[k]][j+dy_h[k]]);
	        				if(map[i+dx_h[k]][j+dy_h[k]]+map[i][j]-2*'A'>maxSum) {
	        					maxSum=map[i+dx_h[k]][j+dy_h[k]]+map[i][j]-2*'A';
	        					maxChar=map[i][j];
	        				}
        				} catch (ArrayIndexOutOfBoundsException e) {
        					continue;
        				}
        			}
        		}
        	}
        }
        // END
        System.out.println(maxChar+" "+maxSum);
        System.out.println(maxChar == 'I' && maxSum == 48);
    }

}
