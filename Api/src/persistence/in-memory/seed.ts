import { Agencia } from "@/domain/agencia/agencia.entity";
import { Cargo } from "@/domain/cargo/cargo.entity";
import { Funcionario } from "@/domain/funcionario/funcionario.entity";
import { AgenciaInMemoryRepository } from "./agencia.repository";
import { CargoInMemoryRepository } from "./cargo.repository";
import { FuncionarioInMemoryRepository } from "./funcionario.repository";
import { PessoaInMemoryRepository } from "./pessoa.repository";

const agencias = AgenciaInMemoryRepository.get();
const cargos = CargoInMemoryRepository.get();
const pessoas = PessoaInMemoryRepository.get();
const funcionarios = FuncionarioInMemoryRepository.get(pessoas);

async function main() {
  const gerente = await cargos.create(
    new Cargo({
      nome: "Gerente",
      permissoes: new Set(["conta.criar", "conta.listar"]),
    })
  );

  const diretor = await cargos.create(
    new Cargo({
      nome: "Diretor",
      permissoes: new Set(["conta.criar", "conta.listar","funcionario.criar","funcionario.listar"]),
    })
  );

  const agencia = await agencias.create(
    new Agencia({
      nome: "Agencia 1",
    })
  );

  const funcionario = await funcionarios.create(
    new Funcionario({
      nome: "Gabriel Silva",
      cpf: "12345678909",
      email: "gabriel.gatinho@gmail.com",
      endereco: "Rua dos Bobos, 123, Bobos, SP",
      telefone: "+5511999999999",
      senha: "123456",
      cargo: gerente,
      agencia,
    })
  );

  agencia.gerente = funcionario;

  await agencias.update(agencia);
}

main();
