import { Story } from "@/_shared/story";
import { Conta } from "../conta.entity";
import { ContaRepository } from "../conta.repository";

export class GetContasStory implements Story<void, Conta[]> {
  constructor(private readonly contaRepository: ContaRepository) {}

  async execute(): Promise<Conta[]> {
    return this.contaRepository.getAll();
  }
}
