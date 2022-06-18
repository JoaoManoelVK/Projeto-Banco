import { Conta } from "./conta.entity";

export interface ContaRepository {
  getAll(): Promise<Conta[]>;
  getByAgencia(agencia: number): Promise<Conta[]>;
  getByAgenciaAndNumero(agencia: number, number: number): Promise<Conta | null>;
  getByTitular(titularId: number): Promise<Conta[]>;
  getById(id: number): Promise<Conta | null>;
  create(conta: Conta): Promise<Conta>;
  update(conta: Conta): Promise<Conta>;
}
