import { Funcionario } from "@/domain/funcionario/funcionario.entity";
import { CadastrarFuncionariosStory } from "@/domain/funcionario/stories/cadastrar-funcionario.story copy";
import { ListarFuncionariosStory } from "@/domain/funcionario/stories/listar-funcionarios.story";
import { CargoInMemoryRepository } from "@/persistence/in-memory/cargo.repository";
import { FuncionarioInMemoryRepository } from "@/persistence/in-memory/funcionario.repository";
import { PessoaInMemoryRepository } from "@/persistence/in-memory/pessoa.repository";
import { Router } from "express";

const router = Router();

router.get("/", async (req, res, next) => {
  try {
    if (!(req.pessoa instanceof Funcionario)) {
      throw new Error("Apenas funcionários podem listar funcionários");
    }

    const funcionariosRepository = FuncionarioInMemoryRepository.get(
      PessoaInMemoryRepository.get()
    );
    const story = new ListarFuncionariosStory(funcionariosRepository);

    res.status(200).json(await story.execute(req.pessoa.agencia.id));
  } catch (error) {
    next(error);
  }
});

router.post("/", async (req, res, next) => {
  try {
    if (!(req.pessoa instanceof Funcionario)) {
      throw new Error("Apenas funcionários podem criar funcionários");
    }

    const story = new CadastrarFuncionariosStory(
      FuncionarioInMemoryRepository.get(PessoaInMemoryRepository.get()),
      CargoInMemoryRepository.get()
    );

    res.status(200).json(
      await story.execute({
        ...req.body,
        diretor: req.pessoa,
      })
    );
  } catch (error) {
    next(error);
  }
});

export default router;
