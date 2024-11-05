package ejercicio1guia;

import java.util.Scanner;


public class Ejercicio1guia {

    public static void main(String[] args) {
        Scanner Entrada = new Scanner(System.in);
        // pregunta el precio del producto original
        System.out.print("ingrese el precio del producto: ");
        float PrecioProducto = Entrada.nextFloat();
        
        System.out.print("Ingrese el descuento que desea realizar al producto: ");
        float Descuento = Entrada.nextFloat();
        
        float PrecioDescuento = (PrecioProducto * Descuento) / 100;
        
        float PrecioFinal = PrecioProducto - PrecioDescuento;
        System.out.println("El precio original es de: " + PrecioProducto);
        
        System.out.println("El descuento a realizar es de %: " + Descuento);

        System.out.println("Resultado del precio es de: " + PrecioFinal);   
        
        float DescuentoVeinte = (float) (PrecioProducto * 0.20);
        
        if (DescuentoVeinte < PrecioDescuento) {
            System.out.println("El descuento realizado es mayor al 20% del valor del producto"); 
        } else if (DescuentoVeinte == PrecioDescuento) {
            System.out.println("El descuento realizado es del 20% lo mismo que el valor del 20% original del producto");
        } else {
            System.out.println("El descuento es menor al 20% del precio original del producto");
         
        
    }
                
        
        
        
        
        
        
    }
    
}
