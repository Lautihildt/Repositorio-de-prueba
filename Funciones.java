package aed;

class Funciones {
    int cuadrado(int x) {
        return (x*x);
    }

    double distancia(double x, double y) {
        return Math.sqrt(x * x+ y * y);
    }

    boolean esPar(int n) {
        if (n%2 == 0 )  
            return true;
        return false;
        }

    boolean esBisiesto(int n) {
        if (n%4 == 0 && n%100 != 0 || n%400 == 0)  
            return true;
        return false;
    }

    int factorialIterativo(int n) {
        int res = 1;
        for (int i = 1; i <= n; i++) {
            res = res * i;
        }return res;
    }

    int factorialRecursivo(int n) {
        if (n==0)
            return 1;
        else 
        return n * factorialRecursivo(n-1);
    }

    boolean esPrimo(int n) {
        for (int i = 2; i<n; i++) {
            if (n%i == 0)
                return false;
        }
        if (n == 0 || n == 1)
            return false;
        return true;
    }

    int sumatoria(int[] numeros) {
        int res = 0;
        for (int i = 0; i < numeros.length; i++) {
            res = res + numeros[i]; 
        } return res;
    }

    int busqueda(int[] numeros, int buscado) {
        for (int i = 0; i < numeros.length; i++) {
            if (buscado == numeros[i])
                return i;
    }   return 0;
}

    boolean tienePrimo(int[] numeros) {
        for (int i = 0; i < numeros.length; i++) {
            if (esPrimo(numeros[i]) == true)
                return true;
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for (int n : numeros) {
            if (n%2 != 0)
                return false;
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        for (int i = 0; i < s1.length(); i++) {
            if (s1.length() > s2.length())
                return false;
            if (s1.charAt(i) != s2.charAt(i))
                return false;
        }
        return true;
    }

    boolean esSufijo(String s1, String s2) {
        for (int i = 1; i <= s1.length(); i++) {
            if (s1.length() > s2.length())
                return false;
            if (s1.charAt(s1.length()-i) != s2.charAt(s2.length()-i))
                return false;
        }
        return true;
    }
}
