import java.util.Scanner;

public class CalculaCuboQuad {

     public static void main(String[] args) {
         int numero;
         Scanner sc = new Scanner(System.in);
         
         do{
             System.out.println("Digite um número: ");
             numero = sc.nextInt();
         } while (numero <= 0);

        int quad = (int) Math.pow(numero, 2);
        System.out.println("O número ao quadrado é " + quad);
        
        int cubo = (int) Math.pow(numero, 3);
        System.out.println("O número ao cubo é " + cubo);
        
        double raiz_quad = Math.sqrt(numero);
        System.out.println("A raiz quadrada do número é " + raiz_quad);
        
        double raiz_cub = Math.cbrt(numero);
        System.out.println("A raiz cúbica do número é " + raiz_cub);
     }

}