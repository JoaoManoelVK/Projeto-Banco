import { Agencia } from "@/domain/agencia/agencia.entity";
import { AgenciaRepository } from "@/domain/agencia/agencia.repository";

let nextId = 1;

export class AgenciaInMemoryRepository implements AgenciaRepository {
  private static instance: AgenciaInMemoryRepository;

  static get() {
    return (this.instance ??= new this());
  }

  primaryIndex = new Map<number, Agencia>();

  async getAll(): Promise<Agencia[]> {
    return Array.from(this.primaryIndex.values());
  }

  async getById(id: number): Promise<Agencia | null> {
    return this.primaryIndex.get(id) ?? null;
  }

  async create(agencia: Agencia): Promise<Agencia> {
    agencia.id = nextId++;
    agencia.createdAt = new Date();
    agencia.updatedAt = new Date();

    this.primaryIndex.set(agencia.id, agencia);

    return agencia;
  }

  async update(agencia: Agencia): Promise<Agencia> {
    agencia.updatedAt = new Date();

    this.primaryIndex.set(agencia.id, agencia);

    return agencia;
  }
}
