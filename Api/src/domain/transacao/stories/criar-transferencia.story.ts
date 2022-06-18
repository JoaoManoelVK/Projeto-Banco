import { ContaRepository } from "@/domain/conta/conta.repository";
import { Pessoa } from "@/domain/pessoa/pessoa.entity";
import { Story } from "@/_shared/story";
import { TransacaoRespository } from "../transacao.repository";
import { Transferencia } from "../transferencia.entity";

export class CriarTransferenciaStory
  implements Story<CriarTransferenciaStory.Input, Transferencia>
{
  constructor(
    private readonly transacaoRepository: TransacaoRespository,
    private readonly contaRepository: ContaRepository
  ) {}

  async execute(input: CriarTransferenciaStory.Input): Promise<Transferencia> {
    const [origem, destino] = await Promise.all([
      this.contaRepository.getById(input.origem),
      this.contaRepository.getById(input.destino),
    ]);

    if (!origem) {
      throw new Error("Conta de origem não encontrada");
    }

    if (origem.titular.id !== input.titular.id) {
      throw new Error("Conta de origem não pertence ao titular");
    }

    if (!destino) {
      throw new Error("Conta de destino não encontrada");
    }

    destino.depositar(origem.saque(input.valor));

    await Promise.all([
      this.contaRepository.update(origem),
      this.contaRepository.update(destino),
    ]);

    return this.transacaoRepository.create(
      new Transferencia({
        valor: input.valor,
        origem,
        destino,
      })
    ) as Promise<Transferencia>;
  }
}

export namespace CriarTransferenciaStory {
  export type Input = {
    origem: number;
    destino: number;
    valor: number;
    titular: Pessoa;
  };
}
