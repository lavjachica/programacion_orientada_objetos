
import java.util.Scanner;


public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bienvenido a la calculadora básica.");
        
        // Capturar los dos números
        System.out.print("Ingresa el primer número: ");
        double numero1 = scanner.nextDouble();

        System.out.print("Ingresa el segundo número: ");
        double numero2 = scanner.nextDouble();

        // Capturar la operación deseada
        System.out.println("Selecciona una operación: suma (+), resta (-), multiplicación (*), división (/)");
        System.out.print("Ingresa tu opción: ");
        char operacion = scanner.next().charAt(0);

        // Variable para almacenar el resultado
        double resultado = 0;
        boolean operacionValida = true;

        // Estructura switch para realizar la operación
        switch (operacion) {
            case '+':
                resultado = numero1 + numero2;
                break;
            case '-':
                resultado = numero1 - numero2;
                break;
            case '*':
                resultado = numero1 * numero2;
                break;
            case '/':
                if (numero2 != 0) {
                    resultado = numero1 / numero2;
                } else {
                    System.out.println("Error: No se puede dividir entre cero.");
                    operacionValida = false;
                }
                break;
            default:
                System.out.println("Operación no válida.");
                operacionValida = false;
        }

        // Mostrar el resultado si la operación fue válida
        if (operacionValida) {
            System.out.println("El resultado de la operación es: " + resultado);
        }

        System.out.println("Gracias por usar la calculadora.");
        scanner.close();
    }
}
