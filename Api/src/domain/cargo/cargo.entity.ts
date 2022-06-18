import { Entity } from "@/_shared/entity";

type Fields = {
  nome: string;
  permissoes: Set<string>;
};

export class Cargo extends Entity implements Fields {
  nome!: string;
  permissoes!: Set<string>;

  constructor(fields: Fields) {
    super();
    Object.assign(this, fields);
  }

  validate() {
    if (!this.nome) {
      throw new Error("Nome inválido");
    }

    if (!this.permissoes) {
      throw new Error("Permissões inválidas");
    }

    return true;
  }

  toJSON() {
    return {
      ...super.toJSON(),
      nome: this.nome,
      permissoes: Array.from(this.permissoes),
    };
  }
}
