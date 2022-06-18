import { Conta } from "../conta/conta.entity";
import { Transacao } from "./transacao.entity";

export type Fields = {
  id?: number;
  valor: number;
  conta: Conta;
};

export class Rendimento extends Transacao {
  valor!: number;
  conta!: Conta;

  constructor(fields: Fields) {
    super();
    Object.assign(this, fields);
    this.validate();
  }

  incluirNoExtrato(conta: Conta): boolean {
    return this.conta.id === conta.id;
  }

  validate(): boolean {
    super.validate();

    if (!this.conta) {
      throw new Error("Conta inválida");
    }

    this.conta.validate();

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      tipo: "RENDIMENTO",
      conta: this.conta.toJSON(),
    };
  }
}
