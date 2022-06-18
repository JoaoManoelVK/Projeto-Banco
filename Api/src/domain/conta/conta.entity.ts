import { Entity } from "@/_shared/entity";
import { Agencia } from "../agencia/agencia.entity";
import { Pessoa } from "../pessoa/pessoa.entity";

export type Fields = {
  id?: number;
  saldo: number;
  agencia: Agencia;
  titular: Pessoa;
};

export abstract class Conta extends Entity implements Fields {
  id!: number;
  readonly agencia!: Agencia;
  readonly titular!: Pessoa;

  protected _saldo!: number;

  constructor(fields: Fields) {
    super();

    const { saldo, ...data } = fields;

    Object.assign(this, data);

    this._saldo = saldo;

    this.validate();
  }

  get saldo() {
    return this._saldo;
  }

  depositar(valor: number) {
    if (valor <= 0) {
      throw new Error("Valor inválido");
    }

    this._saldo += valor;

    return this;
  }

  abstract saque(valor: number): number;

  transferir(valor: number, conta: Conta) {
    conta.depositar(this.saque(valor));
  }

  validate() {
    if (!this.agencia) {
      throw new Error("Agencia inválida");
    }

    if (!this.titular) {
      throw new Error("Titular inválido");
    }

    this.agencia.validate();
    this.titular.validate();

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      id: this.id,
      saldo: this.saldo,
      agencia: this.agencia.toJSON(),
      titular: this.titular.toJSON(),
    };
  }
}
