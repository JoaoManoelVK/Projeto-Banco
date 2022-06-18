import { Story } from "@/_shared/story";
import { Pessoa } from "../pessoa.entity";
import { PessoaRepository } from "../pessoa.repository";

export class CriarPessoaStory
  implements Story<CriarPessoaStory.Input, CriarPessoaStory.Output>
{
  constructor(private readonly pessoaRepository: PessoaRepository) {}

  async execute(
    input: CriarPessoaStory.Input
  ): Promise<CriarPessoaStory.Output> {
    const pessoa = await this.pessoaRepository.create(new Pessoa(input));

    return pessoa.toJSON();
  }
}

export namespace CriarPessoaStory {
  export type Input = {
    nome: string;
    email: string;
    cpf: string;
    telefone: string;
    endereco: string;
    senha: string;
  };

  export type Output = {
    id: number;
    nome: string;
    email: string;
    cpf: string;
    telefone: string;
    endereco: string;
  };
}
