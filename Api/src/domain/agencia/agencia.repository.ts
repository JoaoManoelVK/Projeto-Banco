import { Agencia } from "./agencia.entity";

export interface AgenciaRepository {
  getAll(): Promise<Agencia[]>;
  getById(id: number): Promise<Agencia | null>;
  create(agencia: Agencia): Promise<Agencia>;
}
