import { Pessoa } from "./pessoa.entity";

export interface PessoaRepository {
  /** Cadastra um usuário */
  create(pessoa: Pessoa): Promise<Pessoa>;

  /** Obtém uma pessoa pelo CPF */
  findByCPF(cpf: string): Promise<Pessoa | null>;

  /** Cria ou obtém uma pessoa */
  findOrCreate(pessoa: Pessoa): Promise<Pessoa>;

  findByAuth(cpf: string, senha: string): Promise<Pessoa | null>;

  findById(id: number): Promise<Pessoa | null>;
}
