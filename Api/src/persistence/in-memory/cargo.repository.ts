import { Cargo } from "@/domain/cargo/cargo.entity";
import { CargoRepository } from "@/domain/cargo/cargo.repository";

let nextId = 1;

export class CargoInMemoryRepository implements CargoRepository {
  private static instance: CargoInMemoryRepository;

  static get() {
    return (this.instance ??= new this());
  }

  primaryIndex = new Map<number, Cargo>();

  async getAll(): Promise<Cargo[]> {
    return Array.from(this.primaryIndex.values());
  }

  async getById(id: number): Promise<Cargo | null> {
    return this.primaryIndex.get(id) ?? null;
  }

  async create(cargo: Cargo): Promise<Cargo> {
    cargo.id = nextId++;
    cargo.createdAt = new Date();
    cargo.updatedAt = new Date();

    this.primaryIndex.set(cargo.id, cargo);

    return cargo;
  }
}
