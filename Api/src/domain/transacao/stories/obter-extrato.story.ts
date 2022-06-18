import { Conta } from "@/domain/conta/conta.entity";
import { Story } from "@/_shared/story";
import { Transacao } from "../transacao.entity";
import { TransacaoRespository } from "../transacao.repository";

export class ObterExtrato implements Story<number, Transacao[]> {
  constructor(private readonly transacaoRepository: TransacaoRespository) {}

  async execute(contaId: number): Promise<Transacao[]> {
    return this.transacaoRepository.getByConta(contaId);
  }
}

export namespace ObterExtrato {
  export type Input = Conta;
  export type Output = Transacao[];
}
