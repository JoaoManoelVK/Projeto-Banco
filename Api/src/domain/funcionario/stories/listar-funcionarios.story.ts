import { FuncionarioInMemoryRepository } from "@/persistence/in-memory/funcionario.repository";
import { PessoaInMemoryRepository } from "@/persistence/in-memory/pessoa.repository";
import { Story } from "@/_shared/story";
import { Funcionario } from "../funcionario.entity";
import { FuncionarioRepository } from "../funcionario.repository";

export class ListarFuncionariosStory implements Story<number, Funcionario[]> {
  constructor(public readonly funcionarioRepository: FuncionarioRepository) {}

  async execute(agenciaId: number): Promise<Funcionario[]> {
    return this.funcionarioRepository.getByAgencia(agenciaId);
  }
}
