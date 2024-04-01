package repetitiva;

import java.util.ArrayList;
import java.util.Collections;

public class vector {
    public static void main(String[] args) {
    int v[] = {1,2,3,4,5,6,7,8,9,10,11};
    System.out.println(v[0]);
    ArrayList<Integer> c = new ArrayList();
        c.add(0, 100);
        c.add(1, 10000);
        c.add(2, 300);
        c.add(3, 400);
        c.add(4, 500);
        c.add(5, 600);
        c.add(6, 700);
        System.out.println("El tamaño de la lista es: " +c.size());
        System.out.println(c);
        System.out.println("El valor 1 esta en la lista ? " + c.contains(100));
        Collections.sort(c);
        System.out.println("Ordenando la lista:  " +c);
        c.remove(1); // Se especifica el index a eliminar
        System.out.println("Imprimiendo Lista despues de eliminacion" +c);
        c.clear();
        System.out.println("Imprimiendo Lista despues de vaciada" +c);
        
        

for (int i = 0;i<v.length;i++){
  System.out.println(v[i]);
}
    }
    
}
