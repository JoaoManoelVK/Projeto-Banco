import { Conta, Fields as ContaFields } from "@/domain/conta/conta.entity";

export type Fields = ContaFields & {
  chequeEspecial: number;
};

export class ContaCorrente extends Conta {
  chequeEspecial!: number;

  constructor(fields: Fields) {
    super(fields);
    this.chequeEspecial = fields.chequeEspecial;
    this.validate();
  }

  saque(valor: number) {
    if (valor <= 0) {
      throw new Error("Valor inválido");
    }

    if (valor > this.saldo + this.chequeEspecial) {
      throw new Error("Saldo insuficiente");
    }

    this._saldo -= valor;

    return valor;
  }

  validate() {
    super.validate();

    if (this.chequeEspecial < 0) {
      throw new Error("Cheque especial inválido");
    }

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      tipo: "CORRENTE",
      chequeEspecial: this.chequeEspecial,
    };
  }
}
