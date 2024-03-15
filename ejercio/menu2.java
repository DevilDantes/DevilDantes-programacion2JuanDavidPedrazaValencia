
package selectiva;

import java.util.Scanner;

public class menu2 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int opcion;
        System.out.println("ingrese una opcion: \n 1-personas, \n 2-vehiculos, \n 3-universidades, \n 4-notas, \n 5-salir \n escoge una: ");
        opcion = teclado.nextInt();
        switch (opcion){
            case 1:
                System.out.println("elegiste personas");
                break;
            case 2:
                System.out.println("elegiste vehiculos"  );
                break;
            case 3:
                System.out.println("elegiste universidades"  );
                break;
            case 4:
                System.out.println("elegiste notas");
                break;
            case 5:
                System.out.println("Saliendo");
            default:
                 System.out.print("no hay sistema");
                 break;
        }

        
     
    }
    
}
