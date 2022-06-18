import { Funcionario } from "./funcionario.entity";

export interface FuncionarioRepository {
  getAll(): Promise<Funcionario[]>;
  getByAgencia(agencia: number): Promise<Funcionario[]>;
  create(funcionario: Funcionario): Promise<Funcionario>;
}
