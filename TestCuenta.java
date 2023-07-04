public class TestCuenta {
    public static void main(String[] args) {
        Cuenta c = new Cuenta(7000);
        c.abonar(5000);
        System.out.println(c.obtenerSaldo());

    }
}
