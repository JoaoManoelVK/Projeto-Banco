import { Funcionario } from "@/domain/funcionario/funcionario.entity";
import { FuncionarioRepository } from "@/domain/funcionario/funcionario.repository";
import { PessoaRepository } from "@/domain/pessoa/pessoa.repository";

export class FuncionarioInMemoryRepository implements FuncionarioRepository {
  private static instance: FuncionarioInMemoryRepository;

  static get(pessoaRepository: PessoaRepository) {
    return (this.instance ??= new this(pessoaRepository));
  }

  primaryIndex = new Map<number, Funcionario>();

  constructor(private readonly pessoaRepository: PessoaRepository) {}

  async getAll(): Promise<Funcionario[]> {
    return Array.from(this.primaryIndex.values());
  }

  getByAgencia(agencia: number): Promise<Funcionario[]> {
    const result: Funcionario[] = [];

    for (const funcionario of this.primaryIndex.values()) {
      if (funcionario.agencia.id === agencia) {
        result.push(funcionario);
      }
    }

    return Promise.resolve(result);
  }

  async create(funcionario: Funcionario): Promise<Funcionario> {
    funcionario = (await this.pessoaRepository.create(
      funcionario
    )) as Funcionario;

    this.primaryIndex.set(funcionario.id, funcionario);

    return funcionario;
  }
}
