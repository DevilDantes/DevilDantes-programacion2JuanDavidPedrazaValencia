
import java.util.ArrayList;
import java.util.Collections;

public class actividad {
    public static void main(String[] args) {
         ArrayList<Integer> a = new ArrayList();
         System.out.println(a);
    System.out.println("El tamaño de la lista es: " +a.size());
    System.out.println(a);
    
    
    ArrayList<Integer> z = new ArrayList();
        z.add(0, 1);
        z.add(1, 2);
        z.add(2, 3);
        z.add(3, 4);
        z.add(4, 5);
        System.out.println(z);    
     int primerElemento = z.get(0);
        System.out.println("Primer elemento: " + primerElemento);
        
        int indiceCentral = z.size() / 2;
        int elementoCentral = z.get(indiceCentral);
        System.out.println("Elemento central: " + elementoCentral);
        
        int ultimoElemento = z.get(z.size() - 1);
        
        System.out.println("ultimo elemento: " + ultimoElemento);
        
        ArrayList<String> datosPersonales = new ArrayList<>();

        datosPersonales.add("Juan");
        datosPersonales.add("30"); 
        datosPersonales.add("175 cm"); 
        datosPersonales.add("Soltero"); 
        datosPersonales.add("Calle Principal, Ciudad"); 

        System.out.println("Datos personales:");
        for (String dato : datosPersonales) {
            System.out.println(dato);
            
         
        }
        ArrayList<String> it_companies = new ArrayList<>();
        it_companies.add("Facebook");
        it_companies.add("Google");
        it_companies.add("Microsoft");
        it_companies.add("Apple");
        it_companies.add("IBM");
        it_companies.add("Oracle");
        it_companies.add("Amazon");

        System.out.println("Lista de empresas de tecnologia:");
        System.out.println(it_companies);
        
         it_companies.add(2, "Tesla");

        System.out.println("Lista de empresas de tecnologia:");
        System.out.println(it_companies);
        System.out.println("El valor 1 esta en la lista ? " + it_companies .contains("Amazon")); // Devolvera un verdadero en la consola.
        Collections.sort(it_companies);
        System.out.println("Ordenando la lista:  " +it_companies);
        Collections.reverse(it_companies);
        System.out.println("Lista de empresas de tecnologia en orden descendente:");
        System.out.println(it_companies);
        it_companies.remove(1); // Se especifica el index a eliminar
        System.out.println("Imprimiendo Lista despues de eliminacion" +it_companies);
        it_companies.clear();
System.out.println("Imprimiendo Lista despues de vaciada" +it_companies);

    }
}
    
    

