import { ContaRepository } from "@/domain/conta/conta.repository";
import { Transacao } from "@/domain/transacao/transacao.entity";
import { TransacaoRespository } from "@/domain/transacao/transacao.repository";

let nextId = 1;

export class TransacaoInMemoryRepository implements TransacaoRespository {
  private static instance: TransacaoInMemoryRepository;

  static get(contaRepository: ContaRepository) {
    return (this.instance ??= new this(contaRepository));
  }

  primaryIndex = new Map<number, Transacao>();

  constructor(public readonly contaRepository: ContaRepository) {}

  async create(transacao: Transacao): Promise<Transacao> {
    transacao.id = nextId++;
    transacao.createdAt = new Date()
    transacao.updatedAt = new Date()

    this.primaryIndex.set(transacao.id, transacao);

    return transacao;
  }

  async getAll(): Promise<Transacao[]> {
    return Array.from(this.primaryIndex.values());
  }

  async getByConta(contaId: number): Promise<Transacao[]> {
    const conta = await this.contaRepository.getById(contaId);

    if (!conta) {
      throw new Error("Conta não encontrada");
    }

    return Array.from(this.primaryIndex.values()).filter((transacao) =>
      transacao.incluirNoExtrato(conta)
    );
  }
}
