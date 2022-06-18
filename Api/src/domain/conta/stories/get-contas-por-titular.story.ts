import { Story } from "@/_shared/story";
import { Conta } from "../conta.entity";
import { ContaRepository } from "../conta.repository";

export class GetContasPorPessoaStory implements Story<number, Conta[]> {
  constructor(public readonly contaRepository: ContaRepository) {}

  async execute(pessoaId: number): Promise<Conta[]> {
    return this.contaRepository.getByTitular(pessoaId);
  }
}
