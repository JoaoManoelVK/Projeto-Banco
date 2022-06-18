import { Entity } from "@/_shared/entity";
import { Pessoa } from "../pessoa/pessoa.entity";

export type Fields = {
  nome: string;
  gerente?: Pessoa;
};

export class Agencia extends Entity implements Fields {
  nome!: string;
  gerente?: Pessoa;

  constructor(fields: Fields) {
    super();
    Object.assign(this, fields);

    this.validate();
  }

  validate() {
    if (!this.nome) {
      throw new Error("Nome inválido");
    }

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      nome: this.nome,
    };
  }
}
