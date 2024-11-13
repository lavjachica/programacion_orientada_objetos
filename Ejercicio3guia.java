
package ejercicio3guia;

import java.util.Scanner; 

public class Ejercicio3guia {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        
        System.out.print("Ingrese la cantidad de plata chilena que desea convertir: ");
        float clp = entrada.nextFloat();
        
        System.out.println("Seleccione entre las siguientes opciones: ");
        
        System.out.println("1: Dólares (tipo de cambio = 0.0011)");
        System.out.println("2: Euros (tipo de cambio = 0.00095)");
        System.out.println("3: Yenes (tipo de cambio = 0.15)");
        System.out.println("4: Libras Esterlinas (tipo de cambio = 0.00084)");
        System.out.println("5: Yuanes (tipo de cambio = 0.0073)");
        
        System.out.print("Ingrese su opcion: ");
        int opcion = entrada.nextInt();
        
        float montoConvertido;
        
        switch (opcion) {
            case 1: 
                montoConvertido = (float) (clp * 0.0011);
                System.out.println("El cambio de Peso Chileno a Dolar es de : " + montoConvertido + " dolares");
                break;
            case 2: 
                montoConvertido = (float) (clp * 0.00095);
                System.out.println("El cambio de Peso Chileno a Euros es de : " + montoConvertido + " Euros");
                break;
            case 3:
                montoConvertido = (float) (clp * 0.15);
                System.out.println("El cambio de Peso Chileno a Yenes es de : " + montoConvertido + " Yenes");
                break;
            case 4:
                montoConvertido = (float) (clp * 0.00084);
                System.out.println("El cambio de Peso Chileno a Libras Esterlinas es de : " + montoConvertido + " Libras Esterlinas");
                break;
            case 5:
                montoConvertido = (float) (clp * 0.0073);
                System.out.println("El cambio de Peso Chileno a Yuanes es de : " + montoConvertido + " Yuanes");
                break;
            default :
                System.out.println("Opcion no valid, seleccione porfavor una opcion del 1 al 5.");
            
                
        }
        
    }
    
}
