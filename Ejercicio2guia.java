
package ejercicio2guia;

import java.util.Scanner;



public class Ejercicio2guia {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ingrese su edad: ");
        int edad = entrada.nextInt();
        
        
        
        if (edad < 12 && edad > 0) {
            int precioNiño = 2000;
            System.out.println("El valor de la entrada para niño es de " + precioNiño);
        } else if (edad >= 12 && edad <= 17) {
            int precioAdolescente = 3500;
            System.out.println("El valor de la entrada para adolescentes es de " + precioAdolescente);   
        } else {
            int precioAdulto = 5000;
            System.out.println("El valor de la entrada para adulto es de " + precioAdulto);
        }
    }
    
}
