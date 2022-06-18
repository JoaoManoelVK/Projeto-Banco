import { AgenciaRepository } from "@/domain/agencia/agencia.repository";
import { CargoRepository } from "@/domain/cargo/cargo.repository";
import { CriarPessoaStory } from "@/domain/pessoa/stories/create-pessoa.story";
import { Story } from "@/_shared/story";
import { Funcionario } from "../funcionario.entity";
import { FuncionarioRepository } from "../funcionario.repository";

export class CadastrarFuncionariosStory
  implements Story<CadastrarFuncionariosStory.Input, Funcionario>
{
  constructor(
    public readonly funcionarioRepository: FuncionarioRepository,
    public readonly cargoRepository: CargoRepository
  ) {}

  async execute(input: CadastrarFuncionariosStory.Input): Promise<Funcionario> {
    const cargo = await this.cargoRepository.getById(input.cargo);

    if (!cargo) {
      throw new Error("Cargo não encontrado");
    }

    return this.funcionarioRepository.create(
      new Funcionario({
        ...input,
        cargo,
        agencia: input.diretor.agencia,
      })
    );
  }
}

export namespace CadastrarFuncionariosStory {
  export type Input = CriarPessoaStory.Input & {
    cargo: number;
    diretor: Funcionario;
  };
  export type Output = Funcionario;
}
