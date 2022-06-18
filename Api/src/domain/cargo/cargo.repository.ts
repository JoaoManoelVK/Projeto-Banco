import { Cargo } from "./cargo.entity";

export interface CargoRepository {
  getAll(): Promise<Cargo[]>;
  getById(id: number): Promise<Cargo | null>;
  create(cargo: Cargo): Promise<Cargo>;
}
