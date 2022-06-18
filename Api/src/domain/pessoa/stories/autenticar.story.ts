import crypto from "crypto";
import { Story } from "@/_shared/story";
import { Pessoa } from "../pessoa.entity";
import { PessoaRepository } from "../pessoa.repository";

export class AutenticarPessoaStory
  implements Story<AutenticarPessoaStory.Input, AutenticarPessoaStory.Output>
{
  constructor(public readonly pessoaRepository: PessoaRepository) {}

  async execute(
    input: AutenticarPessoaStory.Input
  ): Promise<AutenticarPessoaStory.Output> {
    const pessoa = await this.pessoaRepository.findByAuth(
      input.cpf,
      input.senha
    );

    if (!pessoa) {
      throw new Error("Usuário ou senha inválidos");
    }

    return {
      pessoa,
      token: Buffer.from(`${crypto.randomBytes(8)}:${pessoa.id}`).toString(
        "base64"
      ),
    };
  }
}

export namespace AutenticarPessoaStory {
  export type Input = {
    cpf: string;
    senha: string;
  };

  export type Output = {
    token: string;
    pessoa: Pessoa;
  };
}
