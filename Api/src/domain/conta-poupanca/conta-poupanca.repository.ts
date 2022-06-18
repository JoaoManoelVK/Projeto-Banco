import { ContaPoupanca } from "./conta-poupanca.entity";

export interface ContaPoupancaRepository {
  getAll(): Promise<ContaPoupanca[]>;
  getById(id: number): Promise<ContaPoupanca | null>;
  getByAgencia(agencia: number): Promise<ContaPoupanca[]>;
  getByAgenciaAndNumero(
    agencia: number,
    number: number
  ): Promise<ContaPoupanca | null>;
  create(conta: ContaPoupanca): Promise<ContaPoupanca>;
  update(conta: ContaPoupanca): Promise<ContaPoupanca>;
}
