import { ContaCorrente } from "@/domain/conta-corrente/conta-corrente.entity";
import { ContaCorrenteRepository } from "@/domain/conta-corrente/conta-corrente.repository";
import { ContaRepository } from "@/domain/conta/conta.repository";

export class ContaCorrenteInMemoryRepository
  implements ContaCorrenteRepository
{
  private static instance: ContaCorrenteInMemoryRepository;

  static get(contaRepository: ContaRepository) {
    return (this.instance ??= new this(contaRepository));
  }

  primaryIndex = new Map<number, ContaCorrente>();

  constructor(public readonly contaRepository: ContaRepository) {}

  async getAll(): Promise<ContaCorrente[]> {
    return Array.from(this.primaryIndex.values());
  }

  async getByAgencia(agencia: number): Promise<ContaCorrente[]> {
    const result: ContaCorrente[] = [];

    for (const conta of this.primaryIndex.values()) {
      if (conta.agencia.id === agencia) {
        result.push(conta);
      }
    }

    return Promise.resolve(result);
  }

  async getByAgenciaAndNumero(
    agencia: number,
    number: number
  ): Promise<ContaCorrente | null> {
    for (const conta of this.primaryIndex.values()) {
      if (conta.agencia.id === agencia && conta.id === number) {
        return conta;
      }
    }

    return null;
  }

  async create(conta: ContaCorrente): Promise<ContaCorrente> {
    const contaCorrente = (await this.contaRepository.create(
      conta
    )) as ContaCorrente;

    this.primaryIndex.set(contaCorrente.id, contaCorrente);

    return contaCorrente;
  }

  async update(conta: ContaCorrente): Promise<ContaCorrente> {
    const contaCorrente = (await this.contaRepository.update(
      conta
    )) as ContaCorrente;

    this.primaryIndex.set(contaCorrente.id, contaCorrente);

    return contaCorrente;
  }
}
