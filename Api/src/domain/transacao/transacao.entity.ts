import { Entity } from "@/_shared/entity";
import { Conta } from "../conta/conta.entity";

export abstract class Transacao extends Entity {
  valor!: number;

  abstract incluirNoExtrato(conta: Conta): boolean;

  validate() {
    if (this.valor <= 0) {
      throw new Error("Valor inválido");
    }

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      valor: this.valor,
    };
  }
}
