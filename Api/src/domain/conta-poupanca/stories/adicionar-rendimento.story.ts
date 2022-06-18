import { CriarRendimentoStory } from "@/domain/transacao/stories/criar-rendimento.story";
import { TransacaoRespository } from "@/domain/transacao/transacao.repository";
import { Story } from "@/_shared/story";
import { ContaPoupancaRepository } from "../conta-poupanca.repository";

export class AdicionarRendimentoStory implements Story<void, void> {
  constructor(
    public readonly contaPoupancaRepository: ContaPoupancaRepository,
    public readonly transacaoRepository: TransacaoRespository
  ) {}

  async execute(): Promise<void> {
    const contas = await this.contaPoupancaRepository.getAll();

    await Promise.all(
      contas.map(async (conta) => {
        return new CriarRendimentoStory(
          this.transacaoRepository,
          this.contaPoupancaRepository
        ).execute({ conta });
      })
    );
  }
}

export namespace AdicionarRendimentoStory {
  export type Input = number;
}
