import { Conta } from "../conta/conta.entity";
import { Transacao } from "./transacao.entity";

export type Fields = {
  id?: number;
  valor: number;
  conta: Conta;
};

export class Saque extends Transacao {
  valor!: number;
  conta!: Conta;

  constructor(fields: Fields) {
    super();
    Object.assign(this, fields);
    this.validate();
  }

  validate(): boolean {
    super.validate();

    if (!this.conta) {
      throw new Error("Conta inválida");
    }

    this.conta.validate();

    return true;
  }

  incluirNoExtrato(conta: Conta): boolean {
    return this.conta.id === conta.id;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      tipo: "SAQUE",
      conta: this.conta.toJSON(),
    };
  }
}
