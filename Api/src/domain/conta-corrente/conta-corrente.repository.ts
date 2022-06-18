import { ContaCorrente } from "./conta-corrente.entity";

export interface ContaCorrenteRepository {
  getAll(): Promise<ContaCorrente[]>;
  getByAgencia(agencia: number): Promise<ContaCorrente[]>;
  getByAgenciaAndNumero(
    agencia: number,
    number: number
  ): Promise<ContaCorrente | null>;
  create(conta: ContaCorrente): Promise<ContaCorrente>;
  update(conta: ContaCorrente): Promise<ContaCorrente>;
}
