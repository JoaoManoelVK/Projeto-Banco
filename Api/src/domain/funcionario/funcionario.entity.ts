import { Agencia } from "../agencia/agencia.entity";
import { Cargo } from "../cargo/cargo.entity";
import { Pessoa, Fields as PessoaFields } from "../pessoa/pessoa.entity";

export type Fields = PessoaFields & {
  id?: number;
  agencia: Agencia;
  cargo: Cargo;
};

export class Funcionario extends Pessoa {
  agencia!: Agencia;
  cargo!: Cargo;

  constructor(fields: Fields) {
    super(fields);

    this.agencia = fields.agencia;
    this.cargo = fields.cargo;

    this.validate();
  }

  validate(): boolean {
    super.validate();

    if (!this.agencia) {
      throw new Error("Agencia inválida");
    }

    if (!this.cargo) {
      throw new Error("Cargo inválido");
    }

    this.agencia.validate();
    this.cargo.validate();

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      tipo: "FUNCIONARIO",
      agencia: this.agencia.toJSON(),
      cargo: this.cargo.toJSON(),
    };
  }
}
