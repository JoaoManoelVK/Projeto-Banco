import { ContaRepository } from "@/domain/conta/conta.repository";
import { Story } from "@/_shared/story";
import { Deposito } from "../deposito.entity";
import { TransacaoRespository } from "../transacao.repository";

export class CriarDepositoStory
  implements Story<CriarDepositoStory.Input, Deposito>
{
  constructor(
    private readonly transacaoRepository: TransacaoRespository,
    private readonly contaRepository: ContaRepository
  ) {}

  async execute(input: CriarDepositoStory.Input): Promise<Deposito> {
    const conta = await this.contaRepository.getById(input.conta);

    if (!conta) {
      throw new Error("Conta não encontrada");
    }

    conta.depositar(input.valor);

    await this.contaRepository.update(conta);

    return this.transacaoRepository.create(
      new Deposito({
        conta,
        valor: input.valor,
      })
    ) as Promise<Deposito>;
  }
}

export namespace CriarDepositoStory {
  export type Input = {
    conta: number;
    valor: number;
  };
}
