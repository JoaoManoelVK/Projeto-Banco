import { Conta } from "../conta/conta.entity";
import { Transacao } from "./transacao.entity";

export type Fields = {
  id?: number;
  valor: number;
  origem: Conta;
  destino: Conta;
};

export class Transferencia extends Transacao {
  valor!: number;
  origem!: Conta;
  destino!: Conta;

  constructor(fields: Fields) {
    super();
    Object.assign(this, fields);
    this.validate();
  }

  incluirNoExtrato(conta: Conta): boolean {
    return this.origem.id === conta.id || this.destino.id === conta.id;
  }

  validate(): boolean {
    super.validate();

    if (!this.origem) {
      throw new Error("Conta de origem inválida");
    }

    if (!this.destino) {
      throw new Error("Conta de destino inválida");
    }

    this.origem.validate();
    this.destino.validate();

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      tipo: "TRANSFERENCIA",
      origem: this.origem.toJSON(),
      destino: this.destino.toJSON(),
    };
  }
}
