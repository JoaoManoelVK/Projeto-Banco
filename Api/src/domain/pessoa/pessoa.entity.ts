import { Entity } from "@/_shared/entity";

export type Fields = {
  nome: string;
  email: string;
  cpf: string;
  telefone: string;
  endereco: string;
  senha: string;
};

export class Pessoa extends Entity {
  nome!: string;
  email!: string;
  cpf!: string;
  telefone!: string;
  endereco!: string;
  senha!: string;

  constructor(fields: Fields) {
    super();
    Object.assign(this, fields);
    this.validate();
  }

  validate() {
    if (!this.nome) {
      throw new Error("Nome inválido");
    }

    if (!this.email) {
      throw new Error("Email inválido");
    }

    if (!this.cpf) {
      throw new Error("CPF inválido");
    }

    if (!this.telefone) {
      throw new Error("Telefone inválido");
    }

    if (!this.endereco) {
      throw new Error("Endereço inválido");
    }

    if (!this.senha) {
      throw new Error("Senha inválida");
    }

    return true;
  }

  toJSON() {
    return Object.assign(super.toJSON(), {
      nome: this.nome,
      email: this.email,
      cpf: this.cpf,
      telefone: this.telefone,
      endereco: this.endereco,
    });
  }
}
