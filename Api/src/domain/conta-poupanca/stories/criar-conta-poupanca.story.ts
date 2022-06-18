import { Story } from "@/_shared/story";
import { ContaPoupanca } from "@/domain/conta-poupanca/conta-poupanca.entity";
import { AgenciaRepository } from "@/domain/agencia/agencia.repository";
import { PessoaRepository } from "@/domain/pessoa/pessoa.repository";
import { Pessoa } from "@/domain/pessoa/pessoa.entity";
import { ContaCorrenteRepository } from "@/domain/conta-corrente/conta-corrente.repository";
import { ContaPoupancaRepository } from "../conta-poupanca.repository";

export class CriarContaPoupancaStory
  implements Story<CriarContaStory.Input, CriarContaStory.Output>
{
  constructor(
    public readonly contaPoupancaRepository: ContaPoupancaRepository,
    public readonly agenciaRepository: AgenciaRepository,
    public readonly pessoaRepository: PessoaRepository
  ) {}

  async execute(input: CriarContaStory.Input): Promise<CriarContaStory.Output> {
    const agencia = await this.agenciaRepository.getById(input.conta.agencia);

    if (!agencia) {
      throw new Error("Agencia não encontrada");
    }

    const titular = await this.pessoaRepository.findOrCreate(
      new Pessoa(input.titular)
    );

    return this.contaPoupancaRepository.create(
      new ContaPoupanca({
        agencia,
        saldo: 0,
        titular,
      })
    );
  }
}

export namespace CriarContaStory {
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

  export type Output = ContaPoupanca;
}
