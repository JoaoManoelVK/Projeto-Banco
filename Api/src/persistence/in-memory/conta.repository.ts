import { Conta } from "@/domain/conta/conta.entity";
import { ContaRepository } from "@/domain/conta/conta.repository";

let nextId = 1;

export class ContaInMemoryRepository implements ContaRepository {
  private static instance: ContaInMemoryRepository;

  static get() {
    return (this.instance ??= new this());
  }

  primaryIndex = new Map<number, Conta>();

  async getAll(): Promise<Conta[]> {
    return Array.from(this.primaryIndex.values());
  }

  async getById(id: number): Promise<Conta | null> {
    return this.primaryIndex.get(id) ?? null;
  }

  async getByAgencia(agencia: number): Promise<Conta[]> {
    const result: Conta[] = [];

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
  ): Promise<Conta | null> {
    for (const conta of this.primaryIndex.values()) {
      if (conta.agencia.id === agencia && conta.id === number) {
        return conta;
      }
    }

    return null;
  }

  async getByTitular(pessoaId: number): Promise<Conta[]> {
    const result: Conta[] = [];

    for (const conta of this.primaryIndex.values()) {
      if (conta.titular.id === pessoaId) {
        result.push(conta);
      }
    }

    return Promise.resolve(result);
  }

  async create(conta: Conta): Promise<Conta> {
    conta.id = nextId++;
    conta.createdAt = new Date();
    conta.updatedAt = new Date();

    this.primaryIndex.set(conta.id, conta);

    return conta;
  }

  async update(data: Conta): Promise<Conta> {
    const contaPoupanca = this.primaryIndex.get(data.id) ?? null;

    if (!contaPoupanca) {
      throw new Error("Conta não encontrada");
    }

    Object.assign(contaPoupanca, data);

    return contaPoupanca;
  }
}
