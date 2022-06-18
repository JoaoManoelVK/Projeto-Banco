import { ContaPoupanca } from "@/domain/conta-poupanca/conta-poupanca.entity";
import { ContaPoupancaRepository } from "@/domain/conta-poupanca/conta-poupanca.repository";
import { ContaRepository } from "@/domain/conta/conta.repository";

export class ContaPoupancaInMemoryRepository
  implements ContaPoupancaRepository
{
  private static instance: ContaPoupancaInMemoryRepository;

  static get(contaRepository: ContaRepository) {
    return (this.instance ??= new this(contaRepository));
  }

  primaryIndex = new Map<number, ContaPoupanca>();

  constructor(public readonly contaRepository: ContaRepository) {}

  async getAll(): Promise<ContaPoupanca[]> {
    return Array.from(this.primaryIndex.values());
  }

  async getById(id: number): Promise<ContaPoupanca | null> {
    return this.primaryIndex.get(id) ?? null;
  }

  async update(conta: ContaPoupanca): Promise<ContaPoupanca> {
    const contaPoupanca = this.primaryIndex.get(conta.id) ?? null;

    if (!contaPoupanca) {
      throw new Error("Conta não encontrada");
    }

    Object.assign(contaPoupanca, conta);

    return contaPoupanca;
  }

  async getByAgencia(agencia: number): Promise<ContaPoupanca[]> {
    const result: ContaPoupanca[] = [];

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
  ): Promise<ContaPoupanca | null> {
    for (const conta of this.primaryIndex.values()) {
      if (conta.agencia.id === agencia && conta.id === number) {
        return conta;
      }
    }

    return null;
  }

  async create(conta: ContaPoupanca): Promise<ContaPoupanca> {
    const contaCorrente = (await this.contaRepository.create(
      conta
    )) as ContaPoupanca;

    this.primaryIndex.set(contaCorrente.id, contaCorrente);

    return contaCorrente;
  }
}
