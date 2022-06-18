import { ContaRepository } from "@/domain/conta/conta.repository";
import { Pessoa } from "@/domain/pessoa/pessoa.entity";
import { Story } from "@/_shared/story";
import { Deposito } from "../deposito.entity";
import { Saque } from "../saque.entity";
import { TransacaoRespository } from "../transacao.repository";

export class CriarSaqueStory implements Story<CriarDepositoStory.Input, Saque> {
  constructor(
    private readonly transacaoRepository: TransacaoRespository,
    private readonly contaRepository: ContaRepository
  ) {}

  async execute(input: CriarDepositoStory.Input): Promise<Saque> {
    const conta = await this.contaRepository.getById(input.conta);

    if (!conta) {
      throw new Error("Conta não encontrada");
    }

    if (conta.titular.id !== input.titular.id) {
      throw new Error("Conta não pertence ao titular");
    }

    conta.saque(input.valor);

    await this.contaRepository.update(conta);

    return this.transacaoRepository.create(
      new Saque({
        conta,
        valor: input.valor,
      })
    ) as Promise<Saque>;
  }
}

export namespace CriarDepositoStory {
  export type Input = {
    conta: number;
    valor: number;
    titular: Pessoa;
  };
}
