import { Story } from "@/_shared/story";
import { Rendimento } from "../rendimento.entity";
import { TransacaoRespository } from "../transacao.repository";
import { ContaPoupancaRepository } from "@/domain/conta-poupanca/conta-poupanca.repository";
import { ContaPoupanca } from "@/domain/conta-poupanca/conta-poupanca.entity";

const TAXA_RENDIMENTO = 0.01; // 1%

export class CriarRendimentoStory
  implements Story<CriarRendimentoStory.Input, Rendimento>
{
  constructor(
    private readonly transacaoRepository: TransacaoRespository,
    private readonly contaRepository: ContaPoupancaRepository
  ) {}

  async execute(input: CriarRendimentoStory.Input): Promise<Rendimento> {
    const conta = input.conta;

    const ganho = conta.saldo * TAXA_RENDIMENTO;

    conta.depositar(ganho);

    await this.contaRepository.update(conta);

    return this.transacaoRepository.create(
      new Rendimento({
        conta,
        valor: ganho,
      })
    ) as Promise<Rendimento>;
  }
}

export namespace CriarRendimentoStory {
  export type Input = {
    conta: ContaPoupanca;
  };
}
