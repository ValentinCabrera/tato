public class Cuenta {
    private double saldo;

    Cuenta(double saldoInicial) {
        this.saldo = saldoInicial > 0 ? saldoInicial : 0;
    }

    public void abonar(double monto) {
        this.saldo = (this.saldo > 0 && monto > 0) ? this.saldo - monto : this.saldo;
    }

    public double obtenerSaldo() {
        return this.saldo;
    }
}