import { Story } from "@/_shared/story";
import { Conta } from "@/domain/conta/conta.entity";
import { ContaCorrenteRepository } from "@/domain/conta-corrente/conta-corrente.repository";
import { ContaCorrente } from "../conta-corrente.entity";
import { AgenciaRepository } from "@/domain/agencia/agencia.repository";
import { PessoaRepository } from "@/domain/pessoa/pessoa.repository";
import { Pessoa } from "@/domain/pessoa/pessoa.entity";

export class CriarContaCorrenteStory
  implements
    Story<CriarContaCorrenteStory.Input, CriarContaCorrenteStory.Output>
{
  constructor(
    public readonly contaCorrenteRepository: ContaCorrenteRepository,
    public readonly agenciaRepository: AgenciaRepository,
    public readonly pessoaRepository: PessoaRepository
  ) {}

  async execute(
    input: CriarContaCorrenteStory.Input
  ): Promise<CriarContaCorrenteStory.Output> {
    const agencia = await this.agenciaRepository.getById(input.conta.agencia);

    if (!agencia) {
      throw new Error("Agencia não encontrada");
    }

    const titular = await this.pessoaRepository.findOrCreate(
      new Pessoa(input.titular)
    );

    return this.contaCorrenteRepository.create(
      new ContaCorrente({
        agencia,
        saldo: 0,
        chequeEspecial: input.conta.chequeEspecial,
        titular,
      })
    );
  }
}

export namespace CriarContaCorrenteStory {
  export type Input = {
    titular: {
      nome: string;
      email: string;
      cpf: string;
      telefone: string;
      endereco: string;
      senha: string;
    };

    conta: {
      agencia: number;
      chequeEspecial: number;
    };
  };

  export type Output = Conta;
}
