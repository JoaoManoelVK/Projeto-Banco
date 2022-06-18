import { Conta } from "@/domain/conta/conta.entity";

export class ContaPoupanca extends Conta {
  saque(valor: number) {
    if (valor <= 0) {
      throw new Error("Valor inválido");
    }

    if (valor > this.saldo) {
      throw new Error("Saldo insuficiente");
    }

    this._saldo -= valor;

    return valor;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      tipo: "POUPANCA",
    };
  }
}
